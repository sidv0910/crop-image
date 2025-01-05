from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .ImageCrop import ImageCrop


def cropImage(request):
    if request.method == "POST":
        files = request.FILES.getlist('file')
        filetype = request.POST.get('type')
        if filetype == 'True' or filetype == 'False':
            filetype = eval(filetype)
        else:
            pass
        cropper = ImageCrop(files, filetype)
        s3_url = cropper.cropImages()
        status = False
        if s3_url.startswith('https://'):
            status = True
        if filetype and status:
            return redirect(s3_url)
        else:
            return render(request, 'download.html', {'url': s3_url, 'status': status})
    else:
        form = FileUploadForm()
        return render(request, 'crop.html', {'form': form})
