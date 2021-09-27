from wtforms import Form, StringField, PasswordField, SubmitField

class RegisterForm(Form):
    username = StringField("")
    firstname = StringField("")
    lastname = StringField("")
    password = PasswordField("")
    conpassword = PasswordField("")
    register = SubmitField("")