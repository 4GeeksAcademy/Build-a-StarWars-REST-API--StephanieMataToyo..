from flask import Flask, request, jsonify, url_for, Blueprint
from models import User, Characters, db, Favourites, Planets, Vehicles
from utils import APIException

api = Blueprint('api', __name__)

@api.route('/user' , methods=['POST'])
def add_user():
    rb = request.get_json()
    user = User(email=rb["email"], user_name=rb["user_name"], is_active=rb["is_active"])
    db.session.add(user)
    db.session.commit()
    return f"User {rb['email']} was added to our data base", 200

@api.route('/user' , methods=['GET'])
def get_all_user():
    user = User.query.all()
    user_list = list(map(lambda User: User.serialize(), user))
    return jsonify(user_list), 200

@api.route('/user/<int:id>', methods=['GET'])
def get_a_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.serialize())

@api.route('/user/<int:id>', methods=['PUT'])
def update_a_user(id):
    user = User.query.get_or_404(id)
    rb = request.get_json()
    if "email" in rb:
        user.email = rb["email"]
    if "user_name" in rb:
        user.user_name = rb["user_name"]
    if "is_active" in rb:
        user.hair_is_active= rb["is_active"]
    db.session.commit()
    return jsonify(user.serialize())

@api.route('/user/<int:id>', methods=['DELETE'])
def delete_a_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return f"User {user.name} was deleted", 200




@api.route('/characters' , methods=['POST'])
def add_characters():
    rb = request.get_json()
    characters = Characters(name=rb["name"], gender=rb["gender"], hair_color=rb["hair_color"], eye_color=rb["eye_color"])
    db.session.add(characters)
    db.session.commit()
    return f"Characters {rb['name']} was added to our data base", 200

@api.route('/characters' , methods=['GET'])
def get_all_characters():
    characters = Characters.query.all()
    characters_list = list(map(lambda Characters: Characters.serialize(), characters))
    return jsonify(characters_list), 200

@api.route('/characters/<int:id>', methods=['GET'])
def get_a_charcaters(id):
    characters = Characters.query.get_or_404(id)
    return jsonify(characters.serialize())

@api.route('/characters/<int:id>', methods=['PUT'])
def update_a_charcaters(id):
    characters = Characters.query.get_or_404(id)
    rb = request.get_json()
    if "name" in rb:
        characters.name = rb["name"]
    if "gender" in rb:
        characters.gender = rb["gender"]
    if "hair_color" in rb:
        characters.hair_color = rb["hair_color"]
    if "eye_color" in rb:
        characters.eye_color = rb["eye_color"]
    db.session.commit()
    return jsonify(characters.serialize())

@api.route('/characters/<int:id>', methods=['DELETE'])
def delete_a_charcaters(id):
    characters = Characters.query.get_or_404(id)
    db.session.delete(characters)
    db.session.commit()
    return f"Characters {characters.name} was deleted", 200



@api.route('/favourites' , methods=['POST'])
def add_favourites():
    rb = request.get_json()
    favourites = Favourites(user_id=rb["user_id"], characters_id=rb["characters_id"], planets_id=rb["planets_id"], vehicles_id=rb["vehicles_id"])
    db.session.add(favourites)
    db.session.commit()
    return f"Favourites {rb['user_id']} was added to our data base", 200

@api.route('/favourites' , methods=['GET'])
def get_all_favourites():
    favourites = Favourites.query.all()
    favourites_list = list(map(lambda Favourites: Favourites.serialize(), favourites))
    return jsonify(favourites_list), 200

@api.route('/favourites/<int:id>', methods=['GET'])
def get_a_favourites(id):
    favourites = Favourites.query.get_or_404(id)
    return jsonify(favourites.serialize())

@api.route('/favourites/<int:id>', methods=['PUT'])
def update_a_favourites(id):
    favourites = Favourites.query.get_or_404(id)
    rb = request.get_json()
    if "user_id" in rb:
        favourites.user_id = rb["user_id"]
    if "characters_id" in rb:
        favourites.characters_id = rb["characters_id"]
    if "planets_id" in rb:
        favourites.planets_id = rb["planets_id"]
    if "vehicles_id" in rb:
        favourites.vehicles_id = rb["vehicles_id"]
    db.session.commit()
    return jsonify(favourites.serialize())

@api.route('/favourites/<int:id>', methods=['DELETE'])
def delete_a_favourites(id):
    favourites = Favourites.query.get_or_404(id)
    db.session.delete(favourites)
    db.session.commit()
    return f"Favourites {favourites.name} was deleted", 200



@api.route('/planets' , methods=['POST'])
def add_planets():
    rb = request.get_json()
    planets = Planets(name=rb["name"], Terrain=rb["Terrain"], population=rb["population"])
    db.session.add(planets)
    db.session.commit()
    return f"Favourites {rb['name']} was added to our data base", 200

@api.route('/planets' , methods=['GET'])
def get_all_planets():
    planets = Planets.query.all()
    planets_list = list(map(lambda Planets: Planets.serialize(), planets))
    return jsonify(planets_list), 200

@api.route('/planets/<int:id>', methods=['GET'])
def get_a_planets(id):
    planets = Planets.query.get_or_404(id)
    return jsonify(planets.serialize())

@api.route('/planets/<int:id>', methods=['PUT'])
def update_a_planets(id):
    planets = Planets.query.get_or_404(id)
    rb = request.get_json()
    if "name" in rb:
        planets.name = rb["name"]
    if "Terrain" in rb:
        planets.Terrain = rb["Terrain"]
    if "population" in rb:
        planets.population = rb["population"]
    db.session.commit()
    return jsonify(planets.serialize())

@api.route('/planets/<int:id>', methods=['DELETE'])
def delete_a_planets(id):
    planets = Planets.query.get_or_404(id)
    db.session.delete(planets)
    db.session.commit()
    return f"Planets {planets.name} was deleted", 200



@api.route('/vehicles' , methods=['POST'])
def add_vehicles():
    rb = request.get_json()
    vehicles = Vehicles(name=rb["name"], model=rb["model"], Cost_in_Credits=rb["Cost_in_Credits"], Crew=rb["Crew"])
    db.session.add(vehicles)
    db.session.commit()
    return f"Vehicles {rb['name']} was added to our data base", 200

@api.route('/vehicles' , methods=['GET'])
def get_all_vehicles():
    vehicles = Vehicles.query.all()
    vehicles_list = list(map(lambda Vehicles: Vehicles.serialize(), vehicles))
    return jsonify(vehicles_list), 200

@api.route('/vehicles/<int:id>', methods=['GET'])
def get_a_vehicles(id):
    vehicles = Vehicles.query.get_or_404(id)
    return jsonify(vehicles.serialize())

@api.route('/vehicles/<int:id>', methods=['PUT'])
def update_a_vehicles(id):
    vehicles = Vehicles.query.get_or_404(id)
    rb = request.get_json()
    if "name" in rb:
        vehicles.name = rb["name"]
    if "model" in rb:
        vehicles.model = rb["model"]
    if "Cost_in_Credits" in rb:
        vehicles.Cost_in_Credits = rb["Cost_in_Credits"]
    if "Crew" in rb:
        vehicles.Crew = rb["Crew"]
    db.session.commit()
    return jsonify(vehicles.serialize())

@api.route('/vehicles/<int:id>', methods=['DELETE'])
def delete_a_planets(id):
    vehicles = Vehicles.query.get_or_404(id)
    db.session.delete(vehicles)
    db.session.commit()
    return f"Vehicles {vehicles.name} was deleted", 200
