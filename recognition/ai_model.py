import os
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import joblib

IMG_SIZE = 128

classes = [
    "Triangle_Medium",
    "Triangle_Bad",
    "Triangle_Perfect",
    "Circle_Irregular",
    "Circle_Medium",
    "Circle_Perfect",
    "Rectangle_Good",
    "Rectangle_Medium",
    "Rectangle_Bad",
]

BASE_DIR = os.path.dirname(__file__)

feature_extractor = load_model(
    os.path.join(BASE_DIR, "models_ai/feature_extractor.h5")
)

lgbm_model = joblib.load(
    os.path.join(BASE_DIR, "models_ai/lgbm_model.pkl")
)


def preprocess_image(img: Image.Image):
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img_array = np.array(img)

    if len(img_array.shape) == 2:
        img_array = np.stack((img_array,) * 3, axis=-1)

    if img_array.shape[-1] != 3:
        img_array = img_array[:, :, :3]

    img_array = img_array / 255.0
    return np.expand_dims(img_array, axis=0)


def predict_shape(img: Image.Image):
    img_array = preprocess_image(img)
    features = feature_extractor.predict(img_array)
    pred_idx = int(lgbm_model.predict(features)[0])

    if pred_idx >= len(classes):
        return "Unknown"

    return classes[pred_idx]
