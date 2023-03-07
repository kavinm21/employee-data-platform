import secrets
import os
import pymysql

host_name = 'mysql-vercel.mysql.database.azure.com'
user_name = 'admin1'
pword = os.environ.get("SQLKey")

add_key = '''
INSERT INTO keystore (
    passkey,
    username
) VALUES({}, {})
'''

get_key_name = '''
SELECT count(*) FROM keystore
WHERE username = '{}'
'''

get_key = '''
SELECT count(*) FROM keystore
WHERE passkey = '{}'
'''

master_key = '''
SELECT username FROM keystore
WHERE passkey = '{}'
'''

table = '''
SELECT username, passkey FROM keystore
'''


class Auth:
    def __init__(self):
        self.connection = None
        try:
            self.connection = pymysql.connect(
                host=host_name, user=user_name, passwd=pword, database='auth',
                 ssl_ca = 'DigiCertGlobalRootCA.crt.pem', ssl_verify_cert = True)
        except Error as err:
            print(f"Error during Authentication: '{err}'")
    def create_key(self, uid):
        try:
            key = secrets.token_urlsafe(16)
            cursor = self.connection.cursor()
            query = add_key.format(key, uid)
            cursor.execute(query)
            cursor.connection.commit()
            cursor.close()
            result = 'Created New Key ' + key  
        except Exception as err:
            result = err
        return result
    def authorize(self, key, uid):
        try:
            cursor = self.connection.cursor()
            if key is not None:
                query = get_key.format(key)
            elif uid is not None:
                query = get_key_name.format(uid)
            else:
                return("No Parameters passed")
            cursor.execute(query)
            query_result = [dict((cursor.description[i][0], value)
                       for i, value in enumerate(row)) for row in cursor.fetchall()]
            output = query_result['count(*)']
            if output != 0:
                result = '1'
            else:
                result = 'Invalid API Key'
        except Exception as err:
            result = err
        return result
    def fetch_keys(self, key):
        try:
            cursor = self.connection.cursor()
            query = master_key.format(key['apikey'])
            cursor.execute(query)
            name = [dict((cursor.description[i][0], value)
                       for i, value in enumerate(row)) for row in cursor.fetchall()][0]['username']
            if name == 'MASTER':
                cursor.execute(table)
                result = [dict((cursor.description[i][0], value)
                       for i, value in enumerate(row)) for row in cursor.fetchall()]
            else:
                result = "Invalid API Key"
        except Exception as err:
            result = err
        return result
    def __del__(self):
        self.connection.close()
        print('Closing MySQL Connection')

def authenticate_user(dict_obj):
    passkey = dict_obj.pop('apikey', '-1')
    if key == '-1':
        return "No Authenication Key Passed", passkey
    msg = Auth().authorize(key=passkey['apikey'])
    return msg, passkey

def get_apis(dict_obj):
    data = Auth().fetch_keys(dict_obj)
    return data

def add_user(dict_obj):
    name = dict_obj.pop('user', '-1')
    if name == '-1':
        return 'Invalid format used'
    if Auth().authorize(uid=name) == 'Invalid API Key':
        msg = Auth().create_key(name)
    else:
        msg = 'Key already present'
    return msg

if __name__ == "__main__":
    a = secrets.token_urlsafe(16)
    print(a, type(a))