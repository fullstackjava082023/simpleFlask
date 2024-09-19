# craete simple flask app
from flask import Flask, request
import os, json



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
    print(f"Received webhook data ", flush=True)
    webhook_data = request.get_json()
    if webhook_data:
        with open('webhook_data.json', 'w') as f:
            json.dump(webhook_data, f, indent=4)
        return 'Webhook received and saved', 200
    return 'Webhook received', 200


# route to show webhook data
@app.route('/webhooks')
def show_webhooks():
    with open('webhook_data.json', 'w') as f:
        webhook_data = json.load(f)
    return f"<pre>{webhook_data}</pre>" 

# route to show log file
@app.route('/log')
def show_log():
    with open('/opt/simpleFlask/app.log', 'r') as f:
        log_data = f.read()
     # Wrap the log data in a <pre> tag to preserve formatting
    return f"<pre>{log_data}</pre>"





if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')