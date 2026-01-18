from flask import Flask
from helper import pets


app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend:</p>
    <ul>
      <li><a href="/animals/dogs">Dogs</a></li>
      <li><a href="/animals/cats">Cats</a></li>
      <li><a href="/animals/rabbits">Rabbits</a></li>
    </ul>
    '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f'<h1>List of {pet_type}</h1>'
    txt = ''
    for pet in pets:
        if pet == pet_type:
            for i, x in enumerate(pets[pet]):
                txt += f'<li><a href="/animals/{pet_type}/{i}">{x}</a></li>'
    txt = '<ul>' + txt + '</ul>'
    return html + txt

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    return f'''
    <h1>{pet['name']}</h1>
    <img src={pet['url']} />
    <p>{pet['description']}</p>
    <ul><li>{pet['breed']}</li><li>{pet['age']}</li></ul>
    '''
