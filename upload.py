import requests

url = "http://localhost:5000/store"
data = {
    "name": "docker3.jpeg",
    "content": "./docker3.jpeg"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json)
