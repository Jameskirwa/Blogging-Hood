from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from ..models import User

class RegistrationForm(FlaskForm):
	email=StringField('Your Email Address',validators=[Required(),Email()])
	username=StringField('Enter your username',validators=[Required()])
	password=PasswordField('Your Password', validators=[Required()])
	password_confirm=PasswordField('Confirm Passwords',validators=[Required()])
	submit= SubmitField('Sign Up')

	def validate_email(self, data_field):
		if User.query.filter_by(email =data_field.data).first():
			raise ValidationError('There is an account with that email')

	def validate_username(self, data_field):
		if User.query.filter_by(username=data_field.data).first():
			raise ValidationError('The usename is taken')

class LoginForm(FlaskForm):
	email =StringField('Your Email Address',validators=[Required(),Email()])
	password = PasswordField('Password',validators =[Required()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Sign In')