import requests

data = {
    "name": "docker3.jpeg",
    "content": "./docker3.jpeg"
}

# Send the POST request to the Flask server
response = requests.post('http://localhost:5000/store', json=data)

# Print the response from the server
print(response.json())
