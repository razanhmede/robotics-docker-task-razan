from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error
import os

app = Flask(__name__)

minio_client = Minio(
    "minio:9000",
    access_key=os.getenv('MINIO_ACCESS_KEY'),
    secret_key=os.getenv('MINIO_SECRET_KEY'),
    secure=False
)

bucket_name = "mybucket"

@app.route('/store', methods=['POST'])
def store():
    data = request.json
    object_name = data.get("name")
    content = data.get("content")

    try:
        minio_client.put_object(bucket_name, object_name, content, len(content))
        return jsonify({"message": "Data stored successfully"}), 200
    except S3Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    app.run(host='0.0.0.0', port=5000)