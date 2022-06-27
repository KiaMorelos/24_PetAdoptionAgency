"""Model for Adoption Agency"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_image_url = "static/imgs/pawprint.png"
##default image from pixabay: Image by Elionas from Pixabay

class Pet(db.Model):
    """Pets Available for Adoption"""
   
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

    @property
    def find_photo(self):
        """Get pet photo or default"""
        return self.photo_url or default_image_url


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)