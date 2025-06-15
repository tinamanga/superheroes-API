from flask import Blueprint, request, jsonify
from . import db
from .models import Hero, Power, HeroPower

# Defining blueprint
api = Blueprint('api', __name__)

# Getting all heroes
@api.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([h.to_dict() for h in heroes])

# Getting one hero by ID
@api.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict())

# Getting all powers
@api.route('/powers', methods=['GET'])
def get_powers():
    return jsonify([p.to_dict() for p in Power.query.all()])

# Getting one power by ID
@api.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict())

# Updating a power description
@api.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    description = data.get("description")

    if not description or len(description) < 20:
        return jsonify({"errors": ["Description must be at least 20 characters long."]}), 400

    try:
        power.description = description
        db.session.commit()
        return jsonify(power.to_dict())
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

# Creating new hero_power
@api.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()

    # Basic validation
    required_fields = ["strength", "power_id", "hero_id"]
    for field in required_fields:
        if field not in data:
            return jsonify({"errors": [f"Missing field: {field}"]}), 400

    try:
        new_hero_power = HeroPower(
            strength=data["strength"],
            power_id=data["power_id"],
            hero_id=data["hero_id"]
        )
        db.session.add(new_hero_power)
        db.session.commit()
        return jsonify(new_hero_power.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400
