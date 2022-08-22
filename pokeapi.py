

from flask import Flask, abort
import csv


with open('pokeparser.csv', 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            pokedatajson = {}
            for pokemon in csvreader:
                pokedatajson.update({pokemon['name']:pokemon})
               

app = Flask(__name__)
  
@app.route('/')
def homepage():
    return '<p>Pokemon Api by Chris S. type pokemon/"pokemonname" for specfic pokemon</p>'

@app.route('/pokemon/<subpath>')
def pokemonpages(subpath):
    
    try:
        return pokedatajson[subpath]
    except KeyError:
        abort(404)


if __name__ == '__main__':


    app.run(use_reloader = True, debug = True)