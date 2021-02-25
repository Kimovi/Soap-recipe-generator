from application import db
from application.models import Soap

db.drop_all()
db.create_all()