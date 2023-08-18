import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for,session,logging,url_for,flash
import pickle
from flask import Markup
import mysql.connector
import os

conn=mysql.connector.connect(host='localhost',port='3306',user='root',password='Onuadejor1',database='register', auth_plugin='mysql_native_password')
cur=conn.cursor()

app = Flask(__name__)
app.secret_key=os.urandom(24)
app.static_folder = 'static'
model = pickle.load(open('model.pkl', 'rb'))
grade = {0: "fair", 1: "good", 2: "poor"}
options = [2, 2, 2, 2, 2, 5, 5, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2]



@app.route('/')
def login():
    return render_template("login.html")

@app.route('/index')
def home():
    if 'id' in session:
        return render_template('index.html')
    else:
        return redirect('/')
    
@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cur.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users = cur.fetchall()
    if len(users)>0:
        session['id']=users[0][0]

        flash('You were successfully logged in')
        return redirect('/index')
    else:
        flash('Invalid credentials !!!')
        return redirect('/')
    # return "The Email is {} and the Password is {}".format(email,password)
    # return render_template('register.html')

@app.route('/add_user',methods=['POST'])
def add_user():
    name=request.form.get('name') 
    email=request.form.get('uemail')
    password=request.form.get('upassword')

    #cur.execute("UPDATE users SET password='{}'WHERE name = '{}'".format(password, name))
    cur.execute("""INSERT INTO  users(name,email,password) VALUES('{}','{}','{}')""".format(name,email,password))
    conn.commit()
    cur.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
    myuser=cur.fetchall()
    flash('You have successfully registered!')
    session['id']=myuser[0][0]
    return redirect('/index')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    arr = np.array([int(x) for x in request.form.values()])
    arr2 = np.array(arr[:15])

    for i, j in zip(options, range(15, 32)):
        temp = np.zeros(i, dtype="int32")
        temp[arr[j]] = 1
        arr2 = np.append(arr2, temp)

    final_features = [np.array(arr2)]
    print(final_features)
    prediction = model.predict(final_features)

    output = grade[prediction[0]]
    print(final_features)
    print(output)

    return render_template('index.html', prediction_text=' Student\'s Final Score should be {} !'.format(output))


@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = grade[prediction[0]]
    return jsonify(output)

@app.route('/register')
def about():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
