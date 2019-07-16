from flask import Flask, render_template, request, abort
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    pokemon = []
    if request.method == 'POST' and 'pokecolour' in request.form:
        colour = request.form.get('pokecolour')
        pokemon = get_poke_colour(colour)


    return render_template('index.html',
                           pokemon=pokemon)


def get_poke_colour(colour):
    r = requests.get('https://pokeapi.co/api/v2/pokemon-color/' + colour.lower())
    pokedata = r.json()
    pokemon = []
    for i in pokedata['pokemon_species']:
        pokemon.append(i['name'])
    return pokemon

if __name__ == '__main__':
    app.run()
