import json
from flask import Flask, jsonify, request,render_template
import csv
import random

with open('pokeparser.csv', 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            pokedatajson = []
            for pokemon in csvreader:
                pokedatajson.append(pokemon)
               
namelist=[]
for pokemon in pokedatajson:
    
        namelist.append(pokemon['name'])

# creating a Flask app
app = Flask(__name__)
  
@app.route('/')
def homepage():
    pokename = random.choice(namelist)
    for pokemon in pokedatajson:
        if pokename in pokemon['name']:
            return jsonify(pokemon)

@app.route('/pokemon/<path:subpath>')
def pokemonpages(subpath):

    for pokemon in pokedatajson:
        if subpath in pokemon['name']:
            
            return jsonify(pokemon)
    # for pokemon in pokedatajson:
    #     if name in pokemon['name']:
            

    #         return jsonify(pokemon)

if __name__ == '__main__':

	# running app
    app.run(use_reloader = True, debug = True)