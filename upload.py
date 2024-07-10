import requests

data = {
    "name": "docker3.jpeg",
    "content": "./docker3.jpeg"
}

# Send the POST request to the Flask server
response = requests.post('http://localhost:5000/store', json=data)

# Check the response status
print(f"Response Status Code: {response.status_code}")

# Check the response content
if response.status_code == 200:
    try:
        print("Response JSON:")
        print(response.json())
    except Exception as e:
        print(f"Failed to parse JSON response: {e}")
else:
    print("Request failed with status code:", response.status_code)
    print("Response Content:", response.text)