from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

@app.route('/square/<int:number>')
def square(number):
    return jsonify({"number": number, "square": number**2})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)
