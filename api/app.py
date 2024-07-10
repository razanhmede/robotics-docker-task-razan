from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error
import os
import base64

app = Flask(__name__)

minio_client = Minio(
    "minio:9000",
    access_key=os.getenv('MINIO_ACCESS_KEY'),
    secret_key=os.getenv('MINIO_SECRET_KEY'),
    secure=False
)

bucket_name = "mybucket"

@app.route('/upload', methods=['POST'])
def upload_file():
    data = request.get_json()
    if not data or 'file_name' not in data or 'file_content' not in data:
        return jsonify({"error": "Invalid request"}), 400
    
    file_name = data['file_name']
    file_content = base64.b64decode(data['file_content'])

    try:
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)
        
        minio_client.put_object(bucket_name, file_name, file_content, len(file_content))
        return jsonify({"message": "File uploaded successfully"}), 200
    except S3Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


