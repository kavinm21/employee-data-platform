import mysql.connector
from mysql.connector import Error

class DB_Ops:
    def __init__(self, host_name, user_name, pword):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(host=host_name,user=user_name,passwd=pword, database='employee_schema')
            print("Connected to MySQL")
        except Error as err:
            print(f"Error: '{err}'")
    def read_emp(self, emp_id):
        cursor = self.connection.cursor()
        query = "SELECT * FROM employee where id = " + str(emp_id)
        cursor.execute(query)
        print(type(cursor))
        cursor.close()
    def __del__(self):
        self.connection.close()
        print('Closing MySQL Connection')

if __name__ == '__main__':
    sql = DB_Ops('127.0.0.1', 'flask', 'flask')
    sql.read_emp(1)