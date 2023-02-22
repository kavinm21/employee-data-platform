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
    send a GET request to  https://employee-data-platform.vercel.app/api/fetchall or https://emp-data-app.azurewebsites.net/api/fetchall

    the data is returned in JSON format
    ```
2. fetchone:
    ```
    send a POST request to https://employee-data-platform.vercel.app/api/fetchone or https://emp-data-app.azurewebsites.net/api/fetchone

    Use content-type as JSON and send a JSON object of the following format:
    {
        "id": <insert employee id here>
    }
    ```
