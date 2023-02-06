from flask import Flask, render_template, request, redirect, session, url_for, jsonify
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

#@app.route('/api/fetchone/<>', methods=['GET', 'POST'])
#def fetch_one():
   

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001, debug=True)
