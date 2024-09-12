# craete simple flask app
from flask import Flask
import os



app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/log')
def show_log():
    return 'showing log file'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')