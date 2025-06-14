from flask import request, jsonify
from app import app, db
from app.models import Hero, Power, HeroPower

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name
    } for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict())
    return jsonify({"error": "Hero not found"}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict())
    return jsonify({"error": "Power not found"}), 404

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    try:
        data = request.get_json()
        power.description = data.get('description')
        db.session.commit()
        return jsonify(power.to_dict())
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    try:
        new_hero_power = HeroPower(
            strength=data.get('strength'),
            power_id=data.get('power_id'),
            hero_id=data.get('hero_id')
        )
        db.session.add(new_hero_power)
        db.session.commit()
        return jsonify(new_hero_power.to_dict()), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
