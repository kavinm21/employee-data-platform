import pymysql
import os

selectall_query = '''
SELECT
    e.id, e.first_name, e.last_name, e.date_of_birth, e.gender, e.employee_role,
    d.department_id, d.department_name, d.employee_salary,
    a.house_no, a.street_name, a.city, a.state, a.country, a.pincode
FROM
    employee e
INNER JOIN department d ON
    e.d_id = d.department_id
INNER JOIN address a ON
    e.id = a.e_id
'''
#host_name = 'rds-mysql.cmmn6yerux7d.ap-south-1.rds.amazonaws.com'
host_name = 'mysql-vercel.mysql.database.azure.com' 
user_name = 'admin1' 
#user_name = 'admin'
pword = os.environ.get("SQLKey")


class DB_Ops:
    def __init__(self):
        self.connection = None
        try:
            self.connection = pymysql.connect(
                host=host_name, user=user_name, passwd=pword, #database='employee_db',
                 ssl_ca = 'DigiCertGlobalRootCA.crt.pem', ssl_verify_cert = True)
            print("Connected to MySQL")
        except Error as err:
            print(f"Error: '{err}'")

    def fetch_one(self, emp_id):
        cursor = self.connection.cursor()
        query = selectall_query + " where e.id = {}".format(emp_id)
        cursor.execute(query)
        result = [dict((cursor.description[i][0], value)
                       for i, value in enumerate(row)) for row in cursor.fetchall()]
        return result
        cursor.close()

    def fetch_all(self):
        cursor = self.connection.cursor()
        cursor.execute(selectall_query)
        result = [dict((cursor.description[i][0], value)
                       for i, value in enumerate(row)) for row in cursor.fetchall()]
        cursor.close()
        return result

    def __del__(self):
        self.connection.close()
        print('Closing RDS MySQL Connection')


if __name__ == '__main__':
    sql = DB_Ops()
    data = sql.fetch_all()
    print(data)
