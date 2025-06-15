from app import create_app, db
from app.models import Hero, Power, HeroPower

app = create_app()

with app.app_context():
    print("Clearing db...")
    db.drop_all()
    db.create_all()

    print("Seeding heroes...")
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
    ]
    db.session.add_all(heroes)

    print("Seeding powers...")
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
    ]
    db.session.add_all(powers)
    db.session.commit()

    print("Seeding hero powers...")
    hp = HeroPower(strength="Strong", hero_id=1, power_id=2)
    db.session.add(hp)

    db.session.commit()
    print("Done seeding!")
