from flask import Flask, jsonify
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    if Earthquake.query.count() == 0:
        db.session.add(Earthquake(location="Chile", magnitude=9.5, year=1960))
        db.session.add(Earthquake(location="Alaska", magnitude=9.2, year=1964))
        db.session.commit()

@app.route('/earthquakes/<int:id>')
def get_earthquake(id):
    quake = Earthquake.query.get(id)
    if quake:
        return jsonify(quake.to_dict())
    else:
        return jsonify({"message": f"Earthquake {id} not found."}), 404

@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    quakes_dict = [q.to_dict() for q in quakes]
    return jsonify({"count": len(quakes), "quakes": quakes_dict})

if __name__ == "__main__":
    app.run(port=5555, debug=True)
