# craete simple flask app
from flask import Flask, request
import os



app = Flask(__name__)

request_counter = 0

@app.route('/')
def hello_world():
    request_counter += 1
    hostname = request.headers.get('Host')
    return f'Hello, World! my server is: {hostname} and request count is: {request_counter}'



@app.route('/log')
def show_log():
    return 'showing log file'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')