from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired,Email
from flask_wtf.file import FileAllowed, FileRequired, FileField 
from flask import Flask, render_template, flash, session, redirect, url_for
from wtforms import TextAreaField, TextField, SubmitField

class UploadForm(FlaskForm):
   description = TextAreaField("Description", validators=[InputRequired("Please enter some small personal information.")])
   photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Only image files accepted.')])