from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('crop/', views.cropImage, name="Crop Image")
]
