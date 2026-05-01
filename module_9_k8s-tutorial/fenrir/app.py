from flask import Flask, render_template
import os

app = Flask(__name__)

PORT = os.environ.get('PORT', 8000) #try to get port number from os otherwise take 8000 port (basically set the port dynamically)

@app.route('/')
def index():

    env = dict(os.environ) #bunch of environment variable in the form of dictionary
    return render_template('index.html', env = env)

if __name__ == '__main__':
    app.run(debug=True , port=PORT, host='0.0.0.0')



# for example :  PORT=9000 app