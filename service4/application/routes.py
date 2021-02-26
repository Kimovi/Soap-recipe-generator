from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/benefit', methods=['POST', "GET"])
def benefit():
    mainIngredient = request.data.decode('utf-8')

    if mainIngredient == "Honey":
        benefit = 'help lighten skin, and reduce wrinkles.'
    elif mainIngredient == "Coffee":
        benefit = 'leaving your skin looking fresh and feeling smooth. Caffeine may also have the benefits of reducing the effects of cellulite and offering a more neutral tone for the skin.'
    elif mainIngredient == "Lavender":
        benefit = 'help lighten skin, and reduce wrinkles.'
    elif mainIngredient == "Orange":
        benefit = 'Antioxidants found in Oranges will brighten your skin'
    elif mainIngredient == "Avocado butter":
        benefit = 'Smooths wrinkles and prevents skin aging.'
    else:
        benefit = 'Green tea contains several vitamins, including vitamin E, which is known for its ability to nourish and hydrate the skin.'

    return Response(benefit, mimetype='text/plain')