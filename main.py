from flask import Flask
from flask import render_template, redirect, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY']='keepthissecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=8000)
