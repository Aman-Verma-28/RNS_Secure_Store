from django.urls import path
from secure_uploads.views import FileUploadAPIView

urlpatterns = [
    path("api/upload/", FileUploadAPIView.as_view(), name="file-upload-api"),
]
# Path: secure_store/secure_uploads/views.py
