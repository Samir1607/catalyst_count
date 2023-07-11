from django.urls import path
from .views import UploadList, UploadCreate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", UploadList.as_view(), name="list"),
    path("create/", UploadCreate.as_view(), name="create"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
