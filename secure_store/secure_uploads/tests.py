import io
from django.test import TestCase, RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import JsonResponse
from secure_uploads.views import FileUploadAPIView

class FileUploadAPITest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_post_with_file(self):
        # Create a test file
        file_content = b"Test file content"
        file = SimpleUploadedFile("test_file.txt", file_content)

        # Create a POST request with the file
        request = self.factory.post("/upload/", {"file": file})

        # Call the view function
        response = FileUploadAPIView.as_view()(request)

        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)

        # Assert that the file was uploaded and encrypted successfully
        expected_message = "File uploaded and encrypted successfully on local filesystem."
        self.assertEqual(response.json(), {"message": expected_message})

        # TODO: Add additional assertions to verify the file was saved correctly

    def test_post_without_file(self):
        # Create a POST request without a file
        request = self.factory.post("/upload/")

        # Call the view function
        response = FileUploadAPIView.as_view()(request)

        # Assert that the response has an error message
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "No file uploaded."})

        # TODO: Add additional assertions to verify the behavior when no file is uploaded