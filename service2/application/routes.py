from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/mainIngredient', methods=['GET'])
def mainIngredient():
    mainIngredient = ["Honey", "Coffee", "Lavender", "Orange", "Avocado butter", "Green tea"]
    return Response(str(random.choice(mainIngredient)), mimetype='text/plain')
