# employee-data-platform
A data store app for fulfilling Cloud Computing Coursework Requirements

# Tech Stack:
SQL, Flask, Python

# API:


Vercel: https://employee-data-platform.vercel.app/

Azure: https://emp-data-app.azurewebsites.net/

URL Suffix     | Functions
-------------  | -------------
/api/fetchall  | Displays all the data in JSON format
/api/fetchone  | Displays data in JSON format given an argument
/api/insertone | Inserts an employee record
/api/delete    | Deletes the employee record

Deploy Branch is deployed to the links mentioned above.
Fetchone and fetchall functionalities are currently active and the rest are under development.

## API Usage:

1. fetchall:

    ```
    send a GET request to 
        https://employee-data-platform.vercel.app/api/fetchall 
        or 
        https://emp-data-app.azurewebsites.net/api/fetchall
    ```
    the data is returned in JSON format

2. fetchone:
    ```
    send a POST request to 
        https://employee-data-platform.vercel.app/api/fetchone 
        or 
        https://emp-data-app.azurewebsites.net/api/fetchone
    ```
    Use content-type as JSON and send a JSON object of the following format:
    ```
    {
        "id": <insert employee id here>
    }
    
    ```
3. addEmp:
    ```
    send a POST request to 
        https://employee-data-platform.vercel.app/api/addEmp 
        or 
        https://emp-data-app.azurewebsites.net/api/addEmp
    ```
    Use content-type as JSON and send a JSON object of the following format:
    ```
    {
        "city": <insert employee city here>,
        "country": <insert employee country here>,
        "date_of_birth": <insert employee dob here>,
        "department_id":  <insert department id here>,
        "department_name": <insert department name here>,
        "employee_role": <insert employee role here>,
        "employee_salary": <insert employee salary here>,
        "first_name": <insert employee first name here>,
        "gender": <insert employee gender here>,
        "house_no": <insert employee's house no. here>,
        "id": <insert employee id here>,
        "last_name": <insert employee last name here>,
        "pincode": <insert employee's pincode here>,
        "state": <insert employee's state here>,
        "street_name": <insert employee's street name here>
    }
    ```
4. delEmp:
    ```
    send a POST request to 
        https://employee-data-platform.vercel.app/api/delEmp 
        or
        https://emp-data-app.azurewebsites.net/api/delEmp
    ``` 
    Use content-type as JSON and send a JSON object of the following format:
    ```
    {
        "id": <insert employee id to be deleted>
    }
    ```
