from django.contrib import admin
from django.urls import path, include

handler404 = 'Home.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('crop/', include('ImageCropper.urls')),
    path('matrix/', include('Matrix.urls')),
]
