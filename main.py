from flask import Flask, session, flash
from flask import request, redirect, url_for
from flask import render_template, g
from flask import make_response

from config import DevelopmentConfig

from flask_wtf import CSRFProtect
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

import forms 
import datetime

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()
mydb = MySQL()

@app.before_request
def fefore_request():
    pages_need_logged = ['index']
    pages_doesnt_need_logged = ['login', 'register']

    if 'username' not in session:
        if request.endpoint in pages_need_logged:
            return redirect( url_for( 'login' ) )
    else:
        if request.endpoint in pages_doesnt_need_logged:
            return redirect( url_for( 'index' ) )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    login_form = forms.LoginForm(request.form)
    
    if request.method == 'POST' and login_form.validate():
        conector = mydb.connect()
        cursor = conector.cursor()

        username = login_form.username.data
        password = login_form.password.data
        
        sentence = 'SELECT password FROM Users WHERE username = %s'
        varibles = (username)
        cursor.execute( sentence, varibles )
        result = cursor.fetchone()

        if result is not None and check_password_hash( result[ 0 ], password ):
            session['username'] = username
            flash( 'welcome {}'.format(username) )
            return redirect( url_for('index') )
        else:
            flash('username or password incorrect')
        
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
        conector = mydb.connect()
        cursor = conector.cursor()

        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        hash_password = generate_password_hash( password )

        sentence = 'INSERT INTO Users(username,email,password,created_date) VALUES(%s,%s,%s,%s)'
        variables = ( username, email, hash_password, datetime.datetime.today() )
        cursor.execute( sentence, variables )
        conector.commit()

        flash("succesful registration")
        return redirect( url_for('login') )

    return render_template('register.html', form=register_form)

if __name__ == '__main__':
    csrf.init_app(app)
    mydb.init_app(app)

    app.run( port=8000 )
