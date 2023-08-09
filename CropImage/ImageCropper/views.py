from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .ImageCrop import ImageCrop


def home(request):
    form = FileUploadForm()
    return render(request, 'home.html', {'form': form})


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def cropImage(request):
    if request.method == "POST":
        files = request.FILES.getlist('file')
        cropper = ImageCrop(files)
        s3_url = cropper.cropImages()
        status = False
        if s3_url.startswith('https://'):
            status = True
        return render(request, 'download.html', {'url': s3_url, 'status': status})
    else:
        return redirect(home)
