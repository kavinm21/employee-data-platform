import pymysql

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
insert_one_dept_query = '''
INSERT INTO
    department (department_id, department_name, employee_salary)
VALUES
({}, {}, {});
'''

insert_one_emp_query = '''
INSERT INTO
    employee (
        id,
        first_name,
        last_name,
        date_of_birth,
        gender,
        d_id,
        employee_role
    )
VALUES
(
        {},
        {},
        {},
        {},
        {},
        {},
        {}
    );
'''

insert_one_addr_query = '''
INSERT INTO
    address (
        e_id,
        house_no,
        street_name,
        city,
        state,
        country,
        pincode
    )
VALUES
(
        {},
        {},
        {},
        {},
        {},
        {},
        {}
    );
'''


host_name = 'rds-mysql.cmmn6yerux7d.ap-south-1.rds.amazonaws.com'
user_name = 'admin'
pword = 'Password1!'


class DB_Ops:
    def __init__(self):
        self.connection = None
        try:
            self.connection = pymysql.connect(
                host=host_name, user=user_name, passwd=pword, database='employee_db')
            print("Connected to MySQL")
        except Error as err:
            print(f"Error: '{err}'")

    def fetch_one(self, emp_id):
        cursor = self.connection.cursor()
        query = selectall_query + " where e.id = %i"
        print(emp_id, " Query:\n", query,sep='')
        cursor.execute(query, (emp_id,))
        result = [dict((cursor.description[i][0], value)
                       for i, value in enumerate(row)) for row in cursor.fetchall()]
        cursor.close()

    def fetch_all(self):
        cursor = self.connection.cursor()
        cursor.execute(selectall_query)
        result = [dict((cursor.description[i][0], value)
                       for i, value in enumerate(row)) for row in cursor.fetchall()]
        cursor.close()
        return result
    
    def insert_one_emp(self, emp_data):
        try:
            cursor = self.connection.cursor()
            query = insert_one_emp_query.format(emp_data['id'],
                                                emp_data['first_name'],
                                                emp_data['last_name'],
                                                emp_data['date_of_birth'],
                                                emp_data['gender'],
                                                emp_data['department_id'],
                                                emp_data['employee_role']
                                               )
            cursor.close()
            result = "Successfully inserted!!"
        except Error as err:
            result = err
#             print(f"Error: '{err}'")
        return result

    def insert_one_dept(self, dept_data):
        try:
            cursor = self.connection.cursor()
            query = insert_one_dept_query.format(dept_data['department_id'],
                                                dept_data['department_name'],
                                                dept_data['employee_salary']
                                                )
            cursor.close()
            result = "Successfully inserted!!"
        except Error as err:
            result = err
            print(f"Error: '{err}'")
        return result
    def insert_one_addr(self, addr_data):
        try:
            cursor = self.connection.cursor()
            query = insert_one_addr_query.format(addr_data['id'],
                                                addr_data['house_no'],
                                                addr_data['street_name'],
                                                addr_data['city'],
                                                addr_data['state'],
                                                addr_data['country'],
                                                addr_data['pincode']
                                                )
            cursor.close()
            result = "Successfully inserted!!"
        except Error as err:
            result = err
            print(f"Error: '{err}'")
        return result

    def __del__(self):
        self.connection.close()
        print('Closing MySQL Connection')


if __name__ == '__main__':
    sql = DB_Ops()
    data = sql.fetch_one('105')
    print(data)
