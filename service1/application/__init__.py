from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="../templates", static_folder='../static')

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////hjkhjkhjkhjk.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@35.230.68.119/Soap"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes