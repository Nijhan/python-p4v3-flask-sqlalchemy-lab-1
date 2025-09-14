from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=False)
    magnitude = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Earthquake {self.location}, Mag: {self.magnitude}>"
