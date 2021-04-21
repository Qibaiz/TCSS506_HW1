#!/usr/local/bin/python3

from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/owner')
def get_owner():
    return 'Hello world from Qibai Zhu'

@app.route('/datetime')
def get_datetime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return f'{dt_string}'

@app.route('/bye')
def goodbye():
    return 'Goodbye'

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
