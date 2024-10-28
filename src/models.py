import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name =  Column(String(50), nullable=False )
    email = Column(String(120), unique=True , nullable=False)
    password = Column(String(50), unique=False , nullable=False)
    is_active = Column(Boolean, unique=False , nullable=False)
    date_joined =  Column(Date, nullable=True)

    favorites = relationship('Favorites', back_populates='user')


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(250), nullable= True)
    climate = Column(String(50), nullable=True)
    terrain = Column(String(50), nullable=True)

    favorites = relationship('Favorites', back_populates='planets')


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(250), nullable= True)
    species = Column(String(50), nullable=True)
    gender = Column(String(50), nullable=True)
    birth_year = Column(String(20), nullable=True)

    favorites = relationship('Favorites', back_populates='people')

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)

    user = relationship('User', back_populates='favorites')
    people = relationship('People', back_populates='favorites')
    planets = relationship('Planets', back_populates='favorites')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
