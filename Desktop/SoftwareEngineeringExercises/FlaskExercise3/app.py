from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)
students={}
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/register', methods = ['GET'])
def display():
    length=len(students)
    return render_template('students.html', students=students, length=length)
@app.route('/register', methods = ['POST'])
def save():
    name = request.form.get('name')
    organization = request.form.get('Organization')
    students[name] = organization
    return redirect('/register')