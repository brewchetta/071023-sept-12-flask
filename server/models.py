from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Park(db.Model):
    
    __tablename__ = 'parks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    size = db.Column(db.Integer)

    animals = db.relationship('Animal', back_populates='park')
    all_species = association_proxy('animals', 'species')


class Animal(db.Model):
    
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.id'))
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))

    park = db.relationship('Park', back_populates='animals')
    species = db.relationship('Species', back_populates='animals')

class Species(db.Model):

    __tablename__ = 'species'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    animals = db.relationship('Animal', back_populates='species')
    parks = association_proxy('animals', 'park')