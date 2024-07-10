from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error
import os

app = Flask(__name__)

minio_client = Minio(
    "minio:9000",
    access_key=os.getenv('MINIO_ACCESS_KEY', 'minioadmin'),
    secret_key=os.getenv('MINIO_SECRET_KEY', 'minioadmin'),
    secure=False
)

bucket_name = "mybucket"

# Check if bucket exists, create it if not
if not minio_client.bucket_exists(bucket_name):
    try:
        minio_client.make_bucket(bucket_name)
    except S3Error as e:
        print(f"Error creating bucket {bucket_name}: {e}")
        # Handle the error appropriately, e.g., log or terminate the app

@app.route('/store', methods=['POST'])
def store():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    object_name = file.filename

    try:
        minio_client.put_object(bucket_name, object_name, file, file.content_length)
        return jsonify({"message": "File stored successfully"}), 200
    except S3Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
