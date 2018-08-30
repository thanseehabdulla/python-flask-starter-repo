from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/joseph')
def hello_joseph():
    nano ={'key':'none','action':'occured','people':'joseph'}
    return json.dumps(nano)

@app.route('/nakul')
def hello_nakul():
    nano ={'key':'none','action':'occured','people':'hai nakul sir'}
    return json.dumps(nano)

@app.route('/thamu')
def hello_thammu():
    data = json.loads('{"key":"none","action":"occured","people":"hai thammu darling"}')
    return data['people']

if __name__ == '__main__':
   app.run(host = "0.0.0.0")