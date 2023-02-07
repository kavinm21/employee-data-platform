import requests

url = 'https://employee-data-platform.vercel.app/api/fetchone'
json = {"id": 105}
x = requests.post(url, json=json)
print(x.json())
