from flask import Flask,jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/about')
def about():
    return "This is my first API"

@app.route('/name')
def name():
    return "John Smith"

@app.route('/skills')
def skills():
    return "Python,Html,Css"

@app.route('/status')
def status():
    return "Learning Flask!"

@app.route('/info')
def info():
    data={
        "name":"John Smith",
        "skills":["Python,HTML,CSS"], #use a list
        "status":"Learning Flask",
        "projects": 0
    }
    return jsonify(data)

@app.route('/portfolio')
def portfolio():
    data={
        "name":"Priya Drashini J S",
        "skills" : ["Python","Flask","Html","Css "], #use seperate qotes for each word
        "projects": 0,
        "github_username" : "priya29o08" #json keys dont have spaces hence use _
    }
    return jsonify(data)

if __name__== '__main__':
    app.run(debug=True)