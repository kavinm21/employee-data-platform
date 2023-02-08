import requests

url = 'http://127.0.0.1:5001/api/addEmp'
json = {
    "city": "Chennai",
    "country": "India",
    "date_of_birth": "2003-02-20 00:00:00",
    "department_id": 100001,
    "department_name": "Finance",
    "employee_role": "Finance Manager",
    "employee_salary": 15000.0,
    "first_name": "Shankar",
    "gender": "Male",
    "house_no": 100,
    "id": 111,
    "last_name": "M",
    "pincode": 641001,
    "state": "TN",
    "street_name": "Srinagar"
}
x = requests.post(url, json=json)
print(x)

'''
url = 'http://127.0.0.1:5001/api/updateDetails'
json = {
    "city" : "Hyderabad",
    "id" : 105
}

x = requests.post(url, json=json)
print(x)
'''
