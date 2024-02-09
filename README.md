# Secure File Storage

## Demo Video Link
[Secure File Storage](https://www.loom.com/share/3612a39d739d479f87d255df688b6470?sid=3876ec17-4514-46f9-b889-f7247458cdd6)

## Description

Secure File Storage is a Django-based application designed to securely handle file uploads, encrypt files, and store them either locally or in AWS S3. This application uses Django Rest Framework for API endpoints, ensuring a robust, scalable solution for managing sensitive files with added encryption for security.

## Features

- File upload via RESTful API.
- File encryption using Fernet symmetric encryption from the Cryptography library.
- Configurable storage options: Local filesystem or AWS S3.
- Simple and secure configuration.

## Getting Started

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django Rest Framework
- Cryptography
- Boto3 (for AWS S3 storage)
- Virtualenv (recommended for creating a virtual environment)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Aman-Verma-28/RNS_Secure_Store.git
   cd secure_store
    ```
2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install the dependencies**

   ```bash
    pip install -r requirements.txt
    ```
4. **Configure the environment variables**

   Create a `.env` file in the root directory and add the following environment variables:

   ```bash
    SECRET_KEY=your_secret_key
    DEBUG=True
    AWS_ACCESS_KEY_ID=your_aws_access_key_id
    AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
    AWS_STORAGE_BUCKET_NAME=your_aws_storage_bucket_name
    AWS_S3_REGION_NAME=your_aws_s3_region_name
    AWS_S3_CUSTOM_DOMAIN=your_aws_s3_custom_domain
    ```
5. **Run the migrations**

   ```bash
   python3 manage.py migrate
   ```
6. **Run the application**

   ```bash
   python3 manage.py runserver
   ```

## Usage

### File Upload
To upload files:

Send a POST request to /api/upload/ with a file in the request body. This can be done using tools like Postman, or via a front-end interface that makes API calls to this endpoint.

Encryption and Storage:

The file will automatically be encrypted and stored in the configured location (local filesystem or AWS S3), based on your settings.py configuration.
