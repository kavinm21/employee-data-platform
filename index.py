from flask import Flask, render_template, request, redirect, session, url_for, jsonify, json
from sql_actions import DB_Ops
app = Flask(__name__)


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('login1.html')

@app.route('/api/fetchall', methods=['GET', 'POST'])
def fetch_all():
    data = DB_Ops().fetch_all()
    return jsonify(data)


@app.route('/api/fetchone', methods=['GET', 'POST'])
def fetch_one():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        id_key = request.json
        data = DB_Ops().fetch_one(id_key['id'])
        return jsonify(data)
    else:
        return 'Content-Type not supported! Send JSON Content'


@app.route('/api/addEmp', methods=['POST', 'GET'])
def add_employee():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        emp_data = request.json
        result_dept = DB_Ops().insert_one_dept(emp_data)
        print(result_dept)
        result_emp = DB_Ops().insert_one_emp(emp_data)
        print(result_emp)
        result_addr = DB_Ops().insert_one_addr(emp_data)
        print(result_addr)
        if result_emp == 'Successfully inserted!!' and result_dept == 'Successfully inserted!!' and result_addr == 'Successfully inserted!!':
            return "Successfully inserted!!"
        else:
            return "Oops!! Failed :/"
    else:
        return 'Content-Type not supported! Send JSON Content'


@app.route('/api/delEmp', methods=['POST', 'GET'])
def delete_details():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        emp_data = request.json
        data = DB_Ops().delete_one(emp_data)
        if data == "Deleted Successfully!!":
            return "Deleted Successfully!!"
        else:
            return 'OOPS!! Failed'
    else:
        return 'Content-Type not supported! Send JSON Content'

@app.route('/api/update', methods=['POST', 'GET'])
def update_details():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        emp_data = request.json
        data = DB_Ops().update(emp_data)
        return data
    else:
        return 'Content-Type not supported! Send JSON Content'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
