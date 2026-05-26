import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# Configuration
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 50
LEARNING_RATE = 0.0001
DATASET_PATH = 'dataset/archive'  # Fixed path to actual dataset
MODEL_SAVE_PATH = 'models/mango_disease_model.h5'

def create_data_generators(dataset_path):
    """Create data generators for training and validation"""
    
    # Data augmentation for training
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        zoom_range=0.2,
        shear_range=0.2,
        fill_mode='nearest',
        validation_split=0.2
    )
    
    # Only rescaling for validation
    val_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )
    
    # Training generator
    train_generator = train_datagen.flow_from_directory(
        dataset_path,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training',
        shuffle=True
    )
    
    # Validation generator
    val_generator = val_datagen.flow_from_directory(
        dataset_path,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation',
        shuffle=False
    )
    
    return train_generator, val_generator

def build_model(num_classes):
    """Build the disease classification model using transfer learning"""
    
    # Load pre-trained MobileNetV2
    base_model = MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    
    # Freeze base model layers initially
    base_model.trainable = False
    
    # Add custom layers
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.2)(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.2)(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    
    # Create final model
    model = Model(inputs=base_model.input, outputs=predictions)
    
    return model, base_model

def unfreeze_base_model(model, base_model, unfreeze_at):
    """Unfreeze layers for fine-tuning"""
    base_model.trainable = True
    
    # Freeze earlier layers
    for layer in base_model.layers[:unfreeze_at]:
        layer.trainable = False
    
    return model

def train_model():
    """Train the disease classification model"""
    
    # Create data generators
    train_gen, val_gen = create_data_generators(DATASET_PATH)
    
    # Get number of classes
    num_classes = len(train_gen.class_indices)
    class_names = list(train_gen.class_indices.keys())
    
    print(f"Number of classes: {num_classes}")
    print(f"Class names: {class_names}")
    
    # Build model
    model, base_model = build_model(num_classes)
    
    # Compile model
    model.compile(
        optimizer=Adam(learning_rate=LEARNING_RATE),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Callbacks
    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=10,
            restore_best_weights=True
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=5,
            min_lr=0.00001
        ),
        tf.keras.callbacks.ModelCheckpoint(
            MODEL_SAVE_PATH,
            monitor='val_accuracy',
            save_best_only=True,
            mode='max'
        )
    ]
    
    # Calculate class weights for balancing
    class_weights = None
    if hasattr(train_gen, 'classes'):
        from sklearn.utils.class_weight import compute_class_weight
        classes = np.unique(train_gen.classes)
        class_weights = compute_class_weight(
            'balanced',
            classes=classes,
            y=train_gen.classes
        )
        class_weights = dict(zip(classes, class_weights))
        print("Class weights calculated:", class_weights)
    
    # Initial training
    print("Phase 1: Training top layers...")
    history1 = model.fit(
        train_gen,
        epochs=10,
        validation_data=val_gen,
        callbacks=callbacks,
        class_weight=class_weights
    )
    
    # Fine-tuning
    print("Phase 2: Fine-tuning...")
    model = unfreeze_base_model(model, base_model, 100)
    
    # Re-compile with lower learning rate
    model.compile(
        optimizer=Adam(learning_rate=LEARNING_RATE/10),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Continue training
    history2 = model.fit(
        train_gen,
        epochs=EPOCHS,
        initial_epoch=history1.epoch[-1],
        validation_data=val_gen,
        callbacks=callbacks
    )
    
    # Combine histories
    history = {
        'accuracy': history1.history['accuracy'] + history2.history['accuracy'],
        'val_accuracy': history1.history['val_accuracy'] + history2.history['val_accuracy'],
        'loss': history1.history['loss'] + history2.history['loss'],
        'val_loss': history1.history['val_loss'] + history2.history['val_loss']
    }
    
    # Save final model
    model.save(MODEL_SAVE_PATH)
    print(f"Model saved to {MODEL_SAVE_PATH}")
    
    return model, history, class_names

def evaluate_model(model, val_gen, class_names):
    """Evaluate the trained model"""
    
    # Get predictions
    val_gen.reset()
    predictions = model.predict(val_gen)
    y_pred = np.argmax(predictions, axis=1)
    y_true = val_gen.classes
    
    # Classification report
    report = classification_report(y_true, y_pred, target_names=class_names)
    print("Classification Report:")
    print(report)
    
    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    
    # Plot confusion matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=class_names, yticklabels=class_names)
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.savefig('confusion_matrix.png')
    plt.close()
    
    return report, cm

def plot_training_history(history):
    """Plot training history"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Accuracy plot
    ax1.plot(history['accuracy'], label='Training Accuracy')
    ax1.plot(history['val_accuracy'], label='Validation Accuracy')
    ax1.set_title('Model Accuracy')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Accuracy')
    ax1.legend()
    ax1.grid(True)
    
    # Loss plot
    ax2.plot(history['loss'], label='Training Loss')
    ax2.plot(history['val_loss'], label='Validation Loss')
    ax2.set_title('Model Loss')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Loss')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('training_history.png')
    plt.close()

def main():
    """Main training function"""
    
    # Check if dataset exists
    if not os.path.exists(DATASET_PATH):
        print(f"Dataset not found at {DATASET_PATH}")
        print("Please ensure your dataset is organized as:")
        print("dataset/")
        print("├── Anthracnose/")
        print("├── Bacterial Canker/")
        print("├── Cutting Weevil/")
        print("├── Die Back/")
        print("├── Gall Midge/")
        print("├── Healthy/")
        print("├── Powdery Mildew/")
        print("└── Sooty Mould/")
        return
    
    # Create models directory
    os.makedirs('models', exist_ok=True)
    
    # Train model
    model, history, class_names = train_model()
    
    # Create data generators for evaluation
    _, val_gen = create_data_generators(DATASET_PATH)
    
    # Evaluate model
    report, cm = evaluate_model(model, val_gen, class_names)
    
    # Plot training history
    plot_training_history(history)
    
    print("Training completed successfully!")
    print(f"Model saved as: {MODEL_SAVE_PATH}")
    print(f"Confusion matrix saved as: confusion_matrix.png")
    print(f"Training history saved as: training_history.png")

if __name__ == "__main__":
    main()
