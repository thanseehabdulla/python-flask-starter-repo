from flask import Flask,redirect, url_for, request
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

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))   

if __name__ == '__main__':
   app.run(host = "0.0.0.0")