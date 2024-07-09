from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error
import os

app = Flask(__name__)

# Initialize MinIO client
minio_client = Minio(
    "minio:9000",
    access_key=os.getenv('MINIO_ACCESS_KEY'),
    secret_key=os.getenv('MINIO_SECRET_KEY'),
    secure=False
)

bucket_name = "mybucket"

# Endpoint to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    object_name = file.filename

    try:
        minio_client.put_object(bucket_name, object_name, file, file.content_length)
        return jsonify({"message": "File uploaded successfully"}), 200
    except S3Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Ensure bucket exists
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
