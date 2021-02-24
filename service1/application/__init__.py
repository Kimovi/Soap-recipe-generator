from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////hjkhjkhjkhjk.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://bora:password@34.82.231.91/Soap"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes