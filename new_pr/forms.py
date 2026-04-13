from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField , SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name = StringField("full name", validators = [DataRequired(message = "Enter your full name ")])
    email = StringField("Email" , validators= [DataRequired(message = "enter your office email"), Email(message= "only valid email is allowed")])
    password = PasswordField("Password" , validators= [DataRequired(message= "password must be 6 charchter"), Length(min= 6, message= "minmum 6 charchter")])
    submit = SubmitField("Register")