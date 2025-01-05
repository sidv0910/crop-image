from django import forms


class MatrixForm(forms.Form):
    subject = forms.CharField(widget=forms.HiddenInput(attrs={'value': '', 'id': 'subject'}), required=True)
    bookletType = forms.CharField(widget=forms.HiddenInput(attrs={'value': '', 'id': 'bookletType'}), required=True)
