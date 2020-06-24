from wtforms import StringField, TextField, PasswordField, BooleanField
from wtforms import Form, validators, HiddenField
from wtforms.fields.html5 import EmailField

def empty_field(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('It must be empty')

class LoginForm(Form):
    username = StringField('Username or Email', [
        validators.Required( message='Required field'),
        validators.length(min=4, max=45, message='Invalid length')
    ])    
    password = PasswordField('Password', [
        validators.Required( message='Required field'),
        validators.length(max=66, message='Invalid length')
    ])
    honeypot = HiddenField('', [ empty_field ])


class RegisterForm(Form):
    username = StringField('Username', [
        validators.Required( message='Required field'),
        validators.length(min=4, max=45, message='Invalid length')
    ])
    email = EmailField('Email', [
        validators.Required( message='Required field'),
        validators.Email( message='Invalid Email'),
        validators.length(min=4, max=45, message='Invalid length')
    ])
    password = PasswordField('Password', [
        validators.Required( message='Required field'),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.length(max=66, message='Invalid length')
    ])
    confirm = PasswordField('Repeat password', [
        validators.Required( message='Required field'),
        validators.length(max=66, message='Invalid length')
    ])
    accept_tos = BooleanField('I accept the TOS', [
        validators.Required( message='Required field')
    ])
    honeypot = HiddenField('', [ empty_field ])
    