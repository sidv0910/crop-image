from django import forms


class FileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'multiple': True, 'accept': '.zip, .png, .jpg, .jpeg',
                                                         'class': 'form-control', 'id': 'formFile'}),
                           required=True)
