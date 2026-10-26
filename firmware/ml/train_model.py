# NeoGuard - TinyML Model Training
# This script will be used to train the 1D-CNN model.
# Full feature extraction (MFCC) is proprietary.

import tensorflow as tf

def build_model():
    model = tf.keras.Sequential([
        # TODO: Add 1D-CNN layers
        tf.keras.layers.Dense(4, activation='softmax')
    ])
    return model

if __name__ == "__main__":
    print("Training pipeline initialized. Waiting for dataset...")
