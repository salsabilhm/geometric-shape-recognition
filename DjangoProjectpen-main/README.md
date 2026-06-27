# 🔷 Geometric Shape Recognition

Intelligent system to recognize hand-drawn geometric shapes and evaluate drawing quality using Deep Learning.

## 🎯 What it does
Upload or capture an image → the system detects:
- **Shape**: Triangle / Rectangle / Circle
- **Quality**: Perfect / Medium / Bad

## 🧠 Model
CNN (Feature Extractor, trained from scratch) + LightGBM → **97.1% accuracy**

| Model | Accuracy |
|-------|----------|
| CNN only | 82.5% |
| VGG16 + Random Forest | 90.8% |
| CNN + Random Forest | 93.9% |
| **CNN + LightGBM ✅** | **97.1%** |

## 🚀 Installation

```bash
git clone https://github.com/salsabilhm/DjangoProjectpen.git
cd DjangoProjectpen
pip install -r requirements.txt
python manage.py runserver
```

Then open: `http://127.0.0.1:8000/recognition/`

## 📁 Project Structure

```
DjangoProjectpen/
├── DjangoProject1/        ← Django config
│   ├── settings.py
│   └── urls.py
├── recognition/           ← Main app
│   ├── ai_model.py        ← CNN + LightGBM logic
│   ├── views.py           ← API endpoints
│   ├── models_ai/         ← Saved models (.h5 + .pkl)
│   ├── templates/         ← HTML pages
│   └── static/            ← CSS files
├── requirements.txt
├── .env.example
└── manage.py
```

## 👥 Authors
M1 SDIA — 2025/2026
