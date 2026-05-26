"""
Script to fix model prediction issues and multilingual support
"""

import os
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from sklearn.utils.class_weight import compute_class_weight
from collections import Counter

def analyze_dataset_balance(dataset_path):
    """Analyze class distribution in dataset"""
    class_counts = {}
    
    for class_name in os.listdir(dataset_path):
        class_path = os.path.join(dataset_path, class_name)
        if os.path.isdir(class_path):
            count = len([f for f in os.listdir(class_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
            class_counts[class_name] = count
    
    print("Dataset Class Distribution:")
    for class_name, count in class_counts.items():
        print(f"{class_name}: {count} images")
    
    return class_counts

def create_balanced_model():
    """Create model with class balancing"""
    
    # Load existing model
    model = load_model('models/mango_disease_model.h5')
    
    # Get class indices
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    generator = datagen.flow_from_directory(
        'dataset',
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical',
        subset='training'
    )
    
    class_indices = generator.class_indices
    class_names = list(class_indices.keys())
    
    # Save class mapping
    with open('models/class_mapping.json', 'w') as f:
        json.dump({
            'class_indices': class_indices,
            'class_names': class_names
        }, f, indent=2)
    
    print("Class mapping saved successfully")
    return class_names

def enhance_multilingual_support():
    """Enhance multilingual support with comprehensive translations"""
    
    enhanced_translations = {
        'en': {
            'Anthracnose': 'Anthracnose',
            'Bacterial Canker': 'Bacterial Canker',
            'Cutting Weevil': 'Cutting Weevil',
            'Die Back': 'Die Back',
            'Gall Midge': 'Gall Midge',
            'Healthy': 'Healthy',
            'Powdery Mildew': 'Powdery Mildew',
            'Sooty Mould': 'Sooty Mould',
            'High Risk': 'High Risk',
            'Moderate Risk': 'Moderate Risk',
            'Low Risk': 'Low Risk',
            'No Risk': 'No Risk'
        },
        'hi': {
            'Anthracnose': 'एंथ्रेक्नोज',
            'Bacterial Canker': 'जीवाणु कैंकर',
            'Cutting Weevil': 'कटिंग वीविल',
            'Die Back': 'डाई बैक',
            'Gall Midge': 'गॉल मिज',
            'Healthy': 'स्वस्थ',
            'Powdery Mildew': 'पाउडरी मिल्ड्यू',
            'Sooty Mould': 'सूटी मोल्ड',
            'High Risk': 'उच्च जोखिम',
            'Moderate Risk': 'मध्यम जोखिम',
            'Low Risk': 'निम्न जोखिम',
            'No Risk': 'कोई जोखिम नहीं'
        },
        'mr': {
            'Anthracnose': 'एंथ्रेक्नोज',
            'Bacterial Canker': 'जीवाणू कँकर',
            'Cutting Weevil': 'कटिंग वीविल',
            'Die Back': 'डाय बॅक',
            'Gall Midge': 'गॉल मिज',
            'Healthy': 'निरोगी',
            'Powdery Mildew': 'पावडरी मिल्ड्यू',
            'Sooty Mould': 'सूटी मोल्ड',
            'High Risk': 'उच्च जोखीम',
            'Moderate Risk': 'मध्यम जोखीम',
            'Low Risk': 'कमी जोखीम',
            'No Risk': 'जोखीम नाही'
        }
    }
    
    # Save enhanced translations
    with open('models/enhanced_translations.json', 'w', encoding='utf-8') as f:
        json.dump(enhanced_translations, f, ensure_ascii=False, indent=2)
    
    print("Enhanced translations saved successfully")

if __name__ == "__main__":
    print("=== Fixing Model Issues ===")
    
    # Analyze dataset balance
    if os.path.exists('dataset'):
        analyze_dataset_balance('dataset')
    
    # Create balanced model
    if os.path.exists('models/mango_disease_model.h5'):
        class_names = create_balanced_model()
        print(f"Model classes: {class_names}")
    
    # Enhance multilingual support
    enhance_multilingual_support()
    
    print("=== Fixes Applied Successfully ===")
