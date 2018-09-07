import json

from flask import Flask, redirect, url_for, request, render_template, session, abort

app = Flask(__name__, template_folder='template')
app.secret_key = "any random string"


@app.route('/')
def index():
    return "<html><body><h1>'Hello This is sample snippet of thanseeh's python flask programming'</h1></body></html>"


@app.route('/joseph')
def hello_joseph():
    nano = {'key': 'none', 'action': 'occured', 'people': 'joseph'}
    return json.dumps(nano)


@app.route('/nakul')
def hello_nakul():
    nano = {'key': 'none', 'action': 'occured', 'people': 'hai nakul sir'}
    # returns the dumps of json object
    return json.dumps(nano)


@app.route('/thamu')
def hello_thammu():
    # loading json into data variable
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


# using both get and post method

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

    # redirect url based on names in python flask


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


# lets render an html folder in flask

@app.route('/renderhtml/<user>')
def renderhtml(user):
    return render_template('hello.html', name=user)


@app.route('/joseph/<int:score>')
def hello_score(score):
    return render_template('mark.html', mark=score)


@app.route('/result')
def result():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result=dict, name='joseph')


# check session
@app.route('/loginsession', methods=['GET', 'POST'])
def loginsession():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))


#    logout as session
@app.route('/logoutsession')
def logoutsession():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))


app.route('/loginrequest', methods=['POST', 'GET'])


def loginrequest():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))


@app.route('/success')
def success():
    return 'logged in successfully'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
