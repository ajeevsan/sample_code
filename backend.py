from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/send-data', methods=['POST'])
def send_data():
    data = request.json.get('inputData')
    print("The Data we get___",data)

    # Process the data as needed
    processed_data = "Processed: " + data
    return jsonify({"receivedData": processed_data})

if __name__ == '__main__':
    app.run(debug=True)
