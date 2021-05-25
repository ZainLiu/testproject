import requests

content = requests.get('http://localhost:3000/')
print(content.content.decode())
