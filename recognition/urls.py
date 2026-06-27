from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict_shape_view, name='predict_shape_view'),  # دالة views.home خاصها تكون موجودة
]

