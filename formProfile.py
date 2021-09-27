from wtforms import Form, StringField, PasswordField, SubmitField

class ProfileForm(Form):
    username = StringField("")
    firstname = StringField("")
    lastname = StringField("")

    currpassword = PasswordField("")
    newpassword = PasswordField("")
    connewpassword = PasswordField("")
    changepassword = SubmitField("")

    modalinputpassword = PasswordField("")
    changeusername = SubmitField("")
    closeacc = SubmitField("")