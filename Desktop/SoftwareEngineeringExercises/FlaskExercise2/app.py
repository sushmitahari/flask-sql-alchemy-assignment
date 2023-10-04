from flask import Flask, render_template, request, redirect
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/calculate', methods = ['POST'])
# def save():
#     global inputValue
#     inputValue=request.form.get('Integer')
#     return redirect('/calculate')
@app.route('/calculate', methods = ['GET'])
def display():
    global inputValue
    inputValue=request.args.get('Integer')
    print(f'Received input: {inputValue}')
    result = ""
    try:
        print("Try")
        number = int(inputValue)
        if number % 2 == 0:
            result = "Even number"
        else:
            result = "Odd number"
    except ValueError:
        result = "Not an integer"
    return render_template('calculate.html', inputValue = inputValue, result = result)