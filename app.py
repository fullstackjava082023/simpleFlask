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
    print(f"Received webhook data", flush=True)
    webhook_data = request.get_json()

    if webhook_data:
        # Extract only repository name and pusher name
        repository_name = webhook_data.get('repository', {}).get('name', 'Unknown repository')
        pusher_name = webhook_data.get('pusher', {}).get('name', 'Unknown pusher')

        # Store only the repository name and pusher name
        filtered_data = {
            'repository_name': repository_name,
            'pusher_name': pusher_name
        }

        # Save the filtered data to a JSON file
        with open('/opt/simpleFlask/webhook_data.json', 'w') as f:
            json.dump(filtered_data, f, indent=4)

        return 'Webhook received and filtered data saved', 200

    return 'Webhook received but no data', 200


# route to show webhook data
@app.route('/webhooks')
def show_webhooks():
    if (os.path.exists('/opt/simpleFlask/webhook_data.json')):
        with open('/opt/simpleFlask/webhook_data.json', 'r') as f:
            webhook_data = json.load(f)
            if webhook_data:
                webhook_data = json.dumps(webhook_data, indent=4)
    else:
        webhook_data = 'No webhook data received yet'
    return webhook_data 

# route to show log file
@app.route('/log')
def show_log():
    with open('/opt/simpleFlask/app.log', 'r') as f:
        log_data = f.read()
     # Wrap the log data in a <pre> tag to preserve formatting
    return f"<pre>{log_data}</pre>"





if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')