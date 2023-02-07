import requests

url = 'http://127.0.0.1:5000/api/addEmp'
json = {"id": 105}
x = requests.post(url, json=json)
print(x)