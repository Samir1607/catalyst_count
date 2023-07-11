from django import forms
from .models import UploadedFile


class UploadForms(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = "__all__"