from rest_framework.views import APIView
from django.http import JsonResponse
from cryptography.fernet import Fernet
import boto3
from django.conf import settings
from .serializers import FileUploadSerializer


class FileUploadAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Access the uploaded file directly
        serializer = FileUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse({"error": "No file uploaded."}, status=400)
        
        uploaded_file = serializer.validated_data["file"]

        # Read the uploaded file
        file_in_memory = uploaded_file.read()

        # Generate a key for encryption
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)

        # Encrypt the file
        encrypted_data = cipher_suite.encrypt(file_in_memory)

        # Save the encrypted file to S3 or local filesystem
        if settings.USE_S3:
            # Upload to S3
            s3 = boto3.client(
                "s3",
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            )
            s3.put_object(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Key=uploaded_file.name,
                Body=encrypted_data,
                ContentType=uploaded_file.content_type,
            )
            return JsonResponse(
                {"message": "File uploaded and encrypted successfully on S3."}
            )
        else:
            # Save to local filesystem
            path = f"../securely_uploaded_file/{uploaded_file.name}" 
            with open(path, "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
            return JsonResponse(
                {
                    "message": "File uploaded and encrypted successfully on local filesystem."
                }
            )
