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

def create_bucket_if_not_exists():
    if not minio_client.bucket_exists(bucket_name):
        try:
            minio_client.make_bucket(bucket_name)
        except S3Error as e:
            print(f"Error creating bucket {bucket_name}: {e}")
            return False
    return True

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    object_name = file.filename

    try:
        if create_bucket_if_not_exists():
            minio_client.put_object(bucket_name, object_name, file, file.content_length)
            return jsonify({"message": "File stored successfully"}), 200
        else:
            return jsonify({"error": "Failed to create or verify bucket"}), 500
    except S3Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    if not create_bucket_if_not_exists():
        print(f"Failed to create or verify bucket {bucket_name}")
    app.run(host='0.0.0.0', port=5000)

