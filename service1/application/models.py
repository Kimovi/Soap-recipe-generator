from application import db

class Soap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mainIngredient = db.Column(db.String(30), nullable=False)
    oilIngredient = db.Column(db.String(30), nullable=False)
    benefit = db.Column(db.String(255), nullable=False)
