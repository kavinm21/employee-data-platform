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

query_dpt = '''SELECT EXISTS(SELECT * FROM department d WHERE d.department_id={})'''

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
({},{},{},{},{},{},{});
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
({},{},{},{},{},{},{});
'''
# DELETE FROM employee.*, address.* from employee e inner join address a on e.id = a.e_id where e.id = {}
delete_one_query = '''
DELETE from employee e where e.id = {}
'''
update_query_emp = '''
update employee
set {}
where id = {}
'''

update_query_dept = '''
update department
set {}
where department_id = {}
'''

update_query_addr = '''
update address
set {}
where e_id = {}
'''


#host_name = 'rds-mysql.cmmn6yerux7d.ap-south-1.rds.amazonaws.com'
host_name = 'mysql-vercel.mysql.database.azure.com'
#user_name = 'admin'
user_name = 'admin1'
pword = os.environ.get("SQLKey")


class DB_Ops:
    def __init__(self):
        self.connection = None
        try:
            self.connection = pymysql.connect(
                host=host_name, user=user_name, passwd=pword, database='employee_db',
                 ssl_ca = 'DigiCertGlobalRootCA.crt.pem', ssl_verify_cert = True)
            print("Connected to MySQL")
        except Error as err:
            print(f"Error: '{err}'")

    def fetch_one(self, id, select_query=selectall_query):
        cursor = self.connection.cursor()
        if select_query == selectall_query:
            query = select_query + " where e.id = {}".format(id)
            cursor.execute(query)
            result = [dict((cursor.description[i][0], value)
                       for i, value in enumerate(row)) for row in cursor.fetchall()]
        else:
             query = select_query.format(id)
             return(cursor.execute(query))
       # print(" Query:\n", query,sep='')
        cursor.close()
        return result

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
                                                "'"+emp_data['first_name']+"'",
                                                "'"+emp_data['last_name']+"'",
                                                "'"+emp_data['date_of_birth']+"'",
                                                "'"+emp_data['gender']+"'",
                                                emp_data['department_id'],
                                                "'"+emp_data['employee_role']+"'"
                                               )
            print(query)
            cursor.execute(query)
            cursor.connection.commit()
            cursor.close()
            result = "Successfully inserted employee!!"
        except Exception as err:
            result = err
#             print(f"Error: '{err}'")
        return result

    def insert_one_dept(self, dept_data):
        try:
            if(self.fetch_one(dept_data['department_id'], query_dpt)==1):
                result = 'Department already exists'
            else:
                cursor = self.connection.cursor()
                query = insert_one_dept_query.format(dept_data['department_id'],
                                                    "'"+dept_data['department_name']+"'",
                                                    dept_data['employee_salary']
                                                    )
                cursor.execute(query)
                cursor.connection.commit()
                cursor.close()
                result = "Successfully inserted department!!"
        except Exception as err:
            result = err
            print(f"Error: '{err}'")
        return result

    def insert_one_addr(self, addr_data):
        try:
            cursor = self.connection.cursor()
            query = insert_one_addr_query.format(addr_data['id'],
                                                addr_data['house_no'],
                                                "'"+addr_data['street_name']+"'",
                                                "'"+addr_data['city']+"'",
                                                "'"+addr_data['state']+"'",
                                                "'"+addr_data['country']+"'",
                                                addr_data['pincode']
                                                )
            print(query)
            cursor.execute(query)
            cursor.connection.commit()
            cursor.close()
            result = "Successfully inserted address!!"
        except Exception as err:
            result = err
            print(f"Error: '{err}'")
        return result

    def delete_one(self, emp_data):
        try:
            cursor = self.connection.cursor()
            query = delete_one_query.format(emp_data['id'])
            cursor.execute(query)
            cursor.connection.commit()
            cursor.close()
            result = "Deleted Successfully!!"
        except Exception as err:
            result = err
            print(f"Error: '{err}'")
        return result

    def update(self, emp_data):
        try:
            up_flag = False
            cursor = self.connection.cursor()
            emp = {key: emp_data[key] for key in ['id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'department_id', 'employee_role']}
            dep = {key: emp_data[key] for key in ['department_id', 'department_name', 'employee_salary']}
            add = {key: emp_data[key] for key in ['id', 'house_no', 'street_name', 'city', 'state', 'country', 'pincode']}
            if 'id' in add.keys():
                add['e_id'] = add.pop('id')
            if len(emp) > 1:
                args = ""
                for key, val in emp.items():
                    if key != 'id':
                        args = args + key + " = '" + val + "', " 
                query = update_query_emp.format(args, emp['id'])
                cursor.execute(query)
                up_flag = True
            if len(add) > 1:
                args = ""
                for key, val in add.items():
                    if key != 'e_id':
                        args = args + key + " = '" + val + "', " 
                query = update_query_emp.format(args, add['e_id'])
                cursor.execute(query)
                up_flag = True
            if len(dep) > 1:
                args = ""
                for key, val in dep.items():
                    if key != 'department_id':
                        args = args + key + " = '" + val + "', " 
                query = update_query_emp.format(args, dep['department_id'])
                cursor.execute(query)
                up_flag = True
            cursor.close()
            if up_flag:
                return "Updated Successfully!!"
            else:
                return "No Update possible, send enough parameters and proper column names"
        except Exception as err:
            result = err
            print(f"Error: '{err}'")
        return result

    def __del__(self):
        self.connection.close()
        print('Closing MySQL Connection')


if __name__ == '__main__':
    sql = DB_Ops()
#     print(data)
