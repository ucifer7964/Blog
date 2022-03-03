
from enum import unique
from flask import Flask,render_template,url_for, flash, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '3320f813d85f022ca5114eeee6997837'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from Flask_Blog import routes