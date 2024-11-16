from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.String)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    def to_dict(self):
        """Custom serialization to ensure correct data types."""
        return {
            "id": self.id,
            "magnitude": float(self.magnitude),  # Explicitly ensure float type
            "location": self.location,
            "year": self.year
        }

    def __repr__(self):
        return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>'