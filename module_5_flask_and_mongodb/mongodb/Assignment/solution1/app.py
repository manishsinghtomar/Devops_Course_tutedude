from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
   response = requests.get('')
    return json_response


if __name__ == '__main__':
    app.run(debug=True)