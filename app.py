from flask import Flask, render_template, request, redirect, session, url_for, jsonify, json
from sql_actions import DB_Ops
app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('login.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
   if request.method == 'GET':
      return redirect(url_for('home'))

   if request.method == 'POST':
      name = request.form['username']
      age = request.form['password']
   return render_template('index.html')

@app.route('/logout')
def logout():
   return redirect(url_for('home'))

@app.route('/display')
def display():
   return render_template('display.html')

@app.route('/update')
def update():
   return render_template('update.html')

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
      return 'Content-httType not supported! Send JSON Content'

@app.route('/api/addEmp', methods=['POST', 'GET'])
def add_student():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        id_key = request.json
        emp_data = jsonify(data)
        result_emp = DB_Ops().insert_one_emp_query(emp_data)
        print(result_emp)
        result_dept = DB_Ops().insert_one_dept_query(emp_data)
        print(result_dept)
        result_addr = DB_Ops().insert_one_addr_query(emp_data)
        print(result_addr)
    if result_emp == 'Successfully inserted!!' and result_dept == 'Successfully inserted!!' and result_addr == 'Successfully inserted!!':
        return "Successfully inserted!!"
    else:
        return "Oops!! Failed :/"


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001, debug=True)
