# employee-data-platform
A data store app for fulfilling Cloud Computing Coursework Requirements

# Tech Stack:
SQL, Flask, Python

# API:


https://employee-data-platform.vercel.app

URL Suffix     | Functions
-------------  | -------------
/api/fetchall  | Displays all the data in JSON format
/api/fetchone  | Displays data in JSON format given an argument
/api/insertone | Inserts an employee record
/api/delete    | Deletes the employee record

branch-aws has been deployed into vercel.
Fetchone and fetchall functionalities are currently active and the rest are under development

## API Usage:

1. fetchall:

    ```
    send a **GET request** to  https://employee-data-platform.vercel.app/api/fetchall
    the data is returned in **JSON format**
    ```
