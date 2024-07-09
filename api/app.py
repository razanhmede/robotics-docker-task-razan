from flask import Flask, request, jsonify, send_from_directory
from minio import Minio
from minio.error import S3Error
import os
import uuid

app = Flask(__name__)

# Initialize MinIO client
minio_client = Minio(
    "minio:9000",
    access_key=os.getenv('MINIO_ACCESS_KEY'),
    secret_key=os.getenv('MINIO_SECRET_KEY'),
    secure=False
)

bucket_name = "mybucket"
upload_folder = 'uploads'  # Folder to store uploaded files

# Endpoint to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    object_name = str(uuid.uuid4()) + '-' + file.filename  # Generate unique object name

    try:
        minio_client.put_object(bucket_name, object_name, file, file.content_length)
        return jsonify({"message": "File uploaded successfully", "file_url": f"http://localhost:5000/uploads/{object_name}"}), 200
    except S3Error as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to serve uploaded files
@app.route('/uploads/<path:filename>')
def serve_file(filename):
    return send_from_directory(upload_folder, filename)

if __name__ == "__main__":
    # Ensure bucket exists
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)

    # Ensure upload folder exists
    os.makedirs(upload_folder, exist_ok=True)

    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)

