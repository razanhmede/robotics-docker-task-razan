from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error
import os
import io

app = Flask(__name__)

# Initialize MinIO client
minio_client = Minio(
    "minio:9000",  # MinIO server address
    access_key=os.getenv('MINIO_ACCESS_KEY'),
    secret_key=os.getenv('MINIO_SECRET_KEY'),
    secure=False
)

bucket_name = "mybucket"

@app.route('/store', methods=['POST'])
def store():
    data = request.json
    
    try:
        object_name = data.get("name")
        content = data.get("content")

        # Check if content is a file path
        if os.path.isfile(content):
            with open(content, 'rb') as file_data:
                # Upload file using fput_object
                minio_client.fput_object(bucket_name, object_name, file_data)
                return jsonify({"message": "File uploaded successfully"}), 200
        else:
            # Assuming content is a text or bytes-like object
            content_bytes = content.encode('utf-8')
            content_stream = io.BytesIO(content_bytes)
            # Upload file using put_object
            minio_client.put_object(bucket_name, object_name, content_stream, len(content))
            return jsonify({"message": "Data uploaded successfully"}), 200

    except S3Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Ensure the bucket exists before starting the server
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    app.run(host='0.0.0.0', port=5000)

