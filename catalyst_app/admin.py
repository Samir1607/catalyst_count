from django.contrib import admin
from .models import UploadedFile


@admin.register(UploadedFile)
class UploadAdmin(admin.ModelAdmin):
    list_display = ["id", "file", "uploaded_at"]
