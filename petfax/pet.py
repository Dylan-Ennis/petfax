from flask import ( Blueprint, render_template ) 
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/<int:pet_id>')
def detail(pet_id):
    pet = next((pet for pet in pets if pet["pet_id"] == pet_id), None)
    if pet:
        return render_template('pet_detail.html', pet=pet)
    else:
        return "Pet not found", 404
    
@bp.route('/submission')
def submit():
    return render_template('submission.html')