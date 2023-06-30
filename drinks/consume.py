import requests
response = requests.get('http://127.0.0.1:8000/drinks')
print(response.json())
print(response.status_code)
print(response.headers)
print(response.headers['Content-Type'])
print(response.text)
print(response.content)
print(response.encoding)