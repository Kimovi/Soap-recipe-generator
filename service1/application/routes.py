from flask import Flask, render_template, request, jsonify
from sqlalchemy import desc
from flask_sqlalchemy import SQLAlchemy
import requests
from application.models import Soap
from application import app, db

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def gen():
    mainIngredient_response = requests.get("http://35.247.62.150:5001/mainIngredient")
    oilIngredient_response = requests.get("http://35.247.62.150:5002/oilIngredient")
    benefit_response = requests.post("http://35.247.62.150:5003/benefit", data = mainIngredient_response.text)

    new_build = Soap(mainIngredient = mainIngredient_response.text, oilIngredient = oilIngredient_response.text, benefit = benefit_response.text)
    db.session.add(new_build)
    db.session.commit()

    return render_template('index.html', mainIngredient=mainIngredient_response.text, oilIngredient=oilIngredient_response.text, benefit=benefit_response.text)