import requests

# File path to the image you want to upload
file_path = '/home/razanhmede/Downloads/session3.jpeg'

# Prepare the files payload
files = {'file': open(file_path, 'rb')}

# Send the POST request to the Flask server
response = requests.post('http://localhost:5000/upload', files=files)

# Print the response from the server
print(response.json())
