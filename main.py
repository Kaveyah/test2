import requests
from flask import Flask, request, jsonify
from db_utils import get_all_pets_db, apply_to_adopt_db, cancel_application_db
app = Flask(__name__)


@app.route('/')
def home():
    return {"message": "Welcome to the Pet Adoption API!"}

@app.route('/pets')
def list_pets():
    return jsonify(get_all_pets_db())


if __name__ == '__main__':
    app.run(debug=True, port=5001)

@app.route("/pets", methods=["GET"])

def list_pets():
    return jsonify(get_all_pets_db())

@app.route("/pets", methods=["POST"])
def adopt_pets():
        data = request.get_json()
        pet_id = data.get('pet_id')
        name = data.get('applicant_name')
        return jsonify(apply_to_adopt_db(pet_id, name))

@app.route('/cancel', methods=['POST'])
def cancel_adopt():
    data = request.get_json()
    pet_id = data.get('pet_id')
    return jsonify(cancel_application_db(pet_id))

if __name__ == '__main__':
    app.run(debug=True, port=5001)

def run():

    print("\n--- Welcome to the Pet Adoption Client ---")
    print("Available pets:")
    pets = requests.get("http://127.0.0.1:5001/pets").json()
    print(pets)