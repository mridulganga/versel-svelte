from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def catch_all(path):
    return "some func"

@app.route('/test1')
def catch_all2(path):
    return "some func 2"