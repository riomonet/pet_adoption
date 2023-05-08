f"""Models for pet adoption."""
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import text 

db = SQLAlchemy()

def connect_db(app):
        db.init_app(app)


class Pets(db.Model):
        """pets for adoption"""

        __tablename__ = 'pets'
        
        id = db.Column(db.Integer, primary_key = True, autoincrement = True)
        name =  db.Column(db.String(50),nullable = False)
        species = db.Column(db.String(50),nullable = False)
        img_url = db.Column(db.String(40), nullable = True)
        age = db.Column(db.Integer)
        comment = db.Column(db.String(200),nullable = True)
        available = db.Column(db.Boolean,nullable = False)

    

