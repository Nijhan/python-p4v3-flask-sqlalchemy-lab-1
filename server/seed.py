from models import db, Earthquake
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    db.session.add(Earthquake(location="Chile", magnitude=9.5, year=1960))
    db.session.add(Earthquake(location="Alaska", magnitude=9.2, year=1964))
    db.session.commit()

    print("Database seeded ✅")
