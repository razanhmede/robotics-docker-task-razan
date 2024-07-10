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
    try:
        data = request.get_json()
        file_name = data.get("file_name")
        file_content_base64 = data.get("file_content")

        if not file_name or not file_content_base64:
            return jsonify({"error": "Missing file_name or file_content"}), 400

        # Decode the Base64 content
        file_content = base64.b64decode(file_content_base64)
        file_size = len(file_content)

        # Save the file to a temporary location
        temp_file_path = f"/tmp/{file_name}"
        with open(temp_file_path, 'wb') as temp_file:
            temp_file.write(file_content)

        # Upload to MinIO
        with open(temp_file_path, 'rb') as temp_file:
            minio_client.put_object(
                bucket_name, file_name, temp_file, file_size
            )
        
        # Remove the temporary file
        os.remove(temp_file_path)

        return jsonify({"message": "File uploaded successfully"}), 200

    except S3Error as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    app.run(host='0.0.0.0', port=5000)
