from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/api')
def get_data():
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
