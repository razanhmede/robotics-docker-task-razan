from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error
import os
import io

app = Flask(__name__)

minio_client = Minio(
    "minio:9000",
    access_key=os.getenv('MINIO_ACCESS_KEY', 'minioadmin'),
    secret_key=os.getenv('MINIO_SECRET_KEY', 'minioadmin'),
    secure=False
)

bucket_name = "mybucket"

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Convert file to bytes and get its size
        file_bytes = file.read()
        file_size = len(file_bytes)
        file_stream = io.BytesIO(file_bytes)

        # Upload to MinIO
        minio_client.put_object(bucket_name, file.filename, file_stream, file_size)
        return jsonify({"message": "File uploaded successfully"}), 200
    except S3Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    app.run(host='0.0.0.0', port=5000)
