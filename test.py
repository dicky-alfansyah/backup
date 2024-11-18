from tensorflow.keras.models import load_model
import os

model_path = 'best_model_densenet201_32303a.h5'

# Fungsi untuk memuat model
def load_the_model():
    try:
        print("Attempting to load the model...")
        model = load_model(model_path)
        print("Model loaded successfully.")
        print("Model summary:")
        print(model.summary())  # Menampilkan summary model
    except Exception as e:
        print(f"Failed to load model: {e}")

# Panggil fungsi
load_the_model()
