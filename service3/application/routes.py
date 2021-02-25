from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/oilIngredient', methods=['GET'])
def oilIngredient():
    oilIngredient = ["Olive oil", "Avocado oil", "Apricot Kernel Oil", "Argan oil", "Black seed oil"]
    return Response(str(random.choice(oilIngredient)), mimetype='text/plain')