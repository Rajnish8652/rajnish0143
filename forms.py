from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,EmailField,PasswordField,SelectField,RadioField
from wtforms.validators import DataRequired
#from PythonProjects.models import demo


class NamerForm(FlaskForm):
    name = StringField('name',render_kw={"placeholder": "Name"})
    password = PasswordField('password',render_kw={"placeholder": "Password"})