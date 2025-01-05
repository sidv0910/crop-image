from django.urls import path
from . import views

urlpatterns = [
    path('', views.matrix, name="Matrix")
]
