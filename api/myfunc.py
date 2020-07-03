from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def catch_all():
    return "test"

@app.route('/test')
def catch_all2():
    return "test2"