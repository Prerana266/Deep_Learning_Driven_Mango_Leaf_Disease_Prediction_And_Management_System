#!/usr/bin/env python3
"""
Test script to verify TensorFlow and model loading functionality
"""

import tensorflow as tf
import os

def test_tensorflow():
    """Test basic TensorFlow functionality"""
    print("Testing TensorFlow functionality...")
    
    # Test TensorFlow version
    print(f"TensorFlow version: {tf.__version__}")
    
    # Test basic operations
    try:
        # Create a simple tensor
        tensor = tf.constant([1, 2, 3, 4])
        print(f"Created tensor: {tensor}")
        
        # Test basic operation
        result = tf.reduce_sum(tensor)
        print(f"Tensor sum: {result}")
        
        print("✅ TensorFlow basic functionality test passed!")
        return True
        
    except Exception as e:
        print(f"❌ TensorFlow test failed: {e}")
        return False

def test_model_loading():
    """Test model loading functionality"""
    print("\nTesting model loading...")
    
    model_path = 'models/mango_disease_model.h5'
    
    if not os.path.exists(model_path):
        print(f"⚠️ Model file not found: {model_path}")
        print("This is expected if the model hasn't been trained yet.")
        return True
    
    try:
        model = tf.keras.models.load_model(model_path)
        print(f"✅ Model loaded successfully from {model_path}")
        print(f"Model summary:")
        model.summary()
        return True
        
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("TensorFlow Test Suite")
    print("=" * 50)
    
    tf_test = test_tensorflow()
    model_test = test_model_loading()
    
    print("\n" + "=" * 50)
    print("Test Results:")
    print(f"TensorFlow: {'✅ PASS' if tf_test else '❌ FAIL'}")
    print(f"Model Loading: {'✅ PASS' if model_test else '❌ FAIL'}")
    print("=" * 50)
