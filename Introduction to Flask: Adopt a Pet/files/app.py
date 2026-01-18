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
    for pt, ps in pets.items():
        if pt == pet_type:
            for i, pet in enumerate(ps):
                html += f'<li><a href="/animals/{pet_type}/{i}">{pet["name"]}</a></li>'
            break
    return '<ul>' + html + '</ul>'

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    return f'''
      <h1>{pet["name"]}</h1>
      <img src={pet["url"]} />
      <ul><li>breed: {pet["breed"]}</li><li>age: {pet["age"]}</li></ul>
    '''
