from flask import Flask, session, flash
from flask import request, redirect, url_for
from flask import render_template, g
from flask import make_response

from config import DevelopmentConfig

from flask_wtf import CSRFProtect
from flaskext.mysql import MySQL

import forms 

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()
mydb = MySQL()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/', methods=['GET','POST'])
def home():
    if 'username' in session:
        return redirect( url_for('index') )
    else:
        return redirect( url_for('login') )

@app.route('/blocknote', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    login_form = forms.LoginForm(request.form)

    cursor = mydb.connect().cursor()
    cursor.execute('SELECT * FROM Users')

    for x in cursor:
        print(x)
    
    if request.method == 'POST' and login_form.validate():
        session['username'] = login_form.username.data
        return redirect( url_for('home') )
    return render_template('login.html',form=login_form )

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect( url_for('login') )

@app.route('/register', methods=['GET','POST'] )
def register():
    
    register_form = forms.RegisterForm(request.form)
    if request.method == 'POST' and register_form.validate():
        flash('Succes registration')
    else:
        flash('fallo :C')

    return render_template('register.html', form=register_form)

if __name__ == '__main__':
    csrf.init_app(app)
    mydb.init_app(app)

    app.run( port=8000 )
