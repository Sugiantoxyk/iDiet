from wtforms import Form, StringField, PasswordField, SubmitField

class LoginForm(Form):
    username = StringField("")
    password = PasswordField("")
    login = SubmitField("")

    adminusername = StringField("")
    adminpassword = PasswordField("")
    adminlogin = SubmitField("")