from django.urls import path
from . import views

urlpatterns = [
    path('', views.cropImage, name="Crop Image")
]
