from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask_wtf import CsrfProtect
import forms 

app = Flask(__name__)
app.secret_key = 'my_secret_key_di_que_eres_puto'
csrf = CsrfProtect(app)

@app.route('/', methods=['GET','POST'] )
def login():
    login_form = forms.LoginForm(request.form)
    return render_template('login.html',form=login_form )

@app.route('/register', methods=['GET','POST'] )
def register():
    register_form = forms.RegisterForm(request.form)
    
    if request.method == 'POST' and register_form.validate():
        print ('paso :D')
    else:
        print ('no paso :C')

    return render_template('register.html', form=register_form)

if __name__ == '__main__':
    app.run( debug=True, port=8000 )
