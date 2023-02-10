import requests

##addEmployee
'''
url = 'http://127.0.0.1:5000/api/addEmp'
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

###Fetch one
'''
url = 'http://127.0.0.1:5000/api/fetchone'
json = {
    "id" : 108
}

x = requests.post(url, json=json)
print(x.text)

'''

#UpdateDetails - Under progress
'''
url = 'http://127.0.0.1:5000/api/updateDetails'
json = {
    "city" : "Hyderabad",
    "id" : 105
}

x = requests.post(url, json=json)
print(x)
'''
#Delete employee
'''
url = 'http://127.0.0.1:5000/api/delEmp'
json = {
    "id" : 111
}
x = requests.post(url, json=json)
print(x)
'''
#UpdateDetails - Under progress
'''
url = 'http://127.0.0.1:5000/api/updateEmp'
json = {
    "id" : 107,
    "last_name":"Umakanthan"
}
x = requests.post(url, json=json)
print(x)
'''
