# 🔷 Geometric Shape Recognition using Deep Learning

An intelligent web-based system for recognizing hand-drawn geometric shapes and evaluating drawing quality using a hybrid Deep Learning and Machine Learning approach.

The project combines a CNN trained from scratch as a feature extractor with a LightGBM classifier and is deployed as a Django web application.

---

#  Project Features

The application allows users to upload an image containing a hand-drawn geometric shape.

The AI model automatically predicts:

- 🔺 Shape Type
  - Triangle
  - Circle
  - Rectangle

-  Drawing Quality
  - Perfect
  - Medium
  - Bad / Irregular

The prediction is displayed instantly through an interactive web interface.

---

#  Dataset

## Dataset Overview

The dataset consists of hand-drawn geometric shapes collected from Kaggle and manually organized for multi-class classification.

Each image belongs to one of three geometric shapes and one of three quality levels, resulting in a total of nine output classes.

### Shape Classes

- Triangle
- Circle
- Rectangle

### Quality Classes

- Perfect
- Medium
- Bad (Irregular)

---

## Dataset Source



## Data Preprocessing

Before training the models, several preprocessing techniques were applied to improve data quality and model performance.

The preprocessing pipeline includes:

- Reading images using OpenCV
- Image resizing to 128 × 128 pixels
- RGB normalization
- Label Encoding
- One-Hot Encoding
- Train / Validation / Test split
- Dataset balancing
- Data Augmentation

These preprocessing steps improve training stability, reduce overfitting, and increase the model's ability to generalize on unseen images.

---

## Data Augmentation

To overcome class imbalance, ImageDataGenerator was used to generate additional training samples.

Applied transformations include:

- Rotation
- Width Shift
- Height Shift
- Zoom
- Horizontal Flip
- Fill Mode

The augmented images were combined with the original dataset to obtain a balanced training set.

---

#  Proposed AI Model

The proposed system follows a hybrid Deep Learning + Machine Learning architecture.

```
Input Image
      │
      ▼
Image Preprocessing
      │
      ▼
CNN Feature Extractor
      │
      ▼
Deep Feature Vector
      │
      ▼
LightGBM Classifier
      │
      ▼
Shape Prediction
+
Drawing Quality Prediction
```

---

## CNN Feature Extractor

Instead of using the CNN as the final classifier, it was trained from scratch to automatically extract high-level visual features from hand-drawn shapes.

The CNN learns:

- Edges
- Curves
- Shape boundaries
- Geometric patterns

The final classification layer was removed after training, allowing the extracted feature vectors to be used by a more powerful machine learning classifier.

---

## LightGBM Classifier

The extracted CNN features are passed to a LightGBM classifier.

LightGBM was selected because it:

- Handles complex decision boundaries efficiently
- Provides fast training and inference
- Improves generalization
- Achieves higher accuracy than traditional classifiers

The combination of CNN Feature Extraction and LightGBM produced the best overall performance.

---

#  Experimental Comparison

Several AI models were evaluated.

| Model | Accuracy |
|------------------------------|----------|
| CNN only | 82.5% |
| CNN + Random Forest | 64.0% |
| VGG16 + SVM | 86.0% |
| VGG16 + Random Forest | 90.8% |
| CNN + Random Forest | 93.9% |
| **CNN + LightGBM** | **97.1%** |

The experimental results demonstrate that CNN Feature Extraction combined with LightGBM significantly outperforms the other evaluated approaches.

---

#  Model Performance

The final model achieved excellent performance across all evaluation metrics.

| Metric | Score |
|----------|------|
| Accuracy | 97.1% |
| Precision | 97% |
| Recall | 97% |
| F1-Score | 97% |

The high values across all evaluation metrics indicate that the model generalizes well and maintains balanced performance across all classes.

---

#  Evaluation Metrics

The repository includes several evaluation figures:

- Accuracy Curve
- Loss Curve
- Classification Report
- Confusion Matrix
- ROC Curve (if available)

---

#  Explainable AI (Grad-CAM)

To improve model interpretability, Grad-CAM visualization was applied.

Grad-CAM highlights the image regions that contributed most to the CNN prediction, allowing users to understand how the model makes its decisions.

This improves transparency and increases confidence in the model's predictions.

---

# 🌐 Web Application

The trained model has been successfully integrated into a Django web application.

Main Features:

- Upload images
- Automatic preprocessing
- AI prediction
- Shape recognition
- Drawing quality assessment
- Real-time results

Frontend:

- HTML
- CSS
- JavaScript

Backend:

- Django

---

#  Technologies Used

- Python
- Django
- TensorFlow / Keras
- LightGBM
- OpenCV
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook


#  Future Improvements

Future versions of this project may include:

- Support for additional geometric shapes
- Real-time camera recognition
- Digital pen integration
- Mobile application deployment
- ONNX / TensorFlow Lite optimization
- Advanced Explainable AI techniques



# Author

**Hamdane Salsabil & Benaissa Roumeissa**

Master 1 – SDIA

2025 / 2026

**Team Project**
