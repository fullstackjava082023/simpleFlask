# craete simple flask app
from flask import Flask, request
import os



app = Flask(__name__)

request_counter = 0

@app.route('/')
def hello_world():
    global request_counter
    request_counter += 1
    hostname = request.headers.get('Host')
    return f'Hello, World! my server is: {hostname} and request count is: {request_counter}'



@app.route('/webhook', methods=['POST'])
def webhook():
    print(f"Received webhook data", flush=True)

    return 'Webhook received', 200


# route to show log file
@app.route('/log')
def show_log():
    with open('app.log', 'r') as f:
        log_data = f.read()
    return log_data


@app.route('/log')
def show_log():
    return 'showing log file'


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')