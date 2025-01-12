import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)

    favorites = relationship('Favorite', back_populates='user')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    climate = Column(String, nullable=True)
    terrain = Column(String, nullable=True)
    population = Column(String, nullable=True)

    favorites = relationship('Favorite', back_populates='planet')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    birth_year = Column(String, nullable=True)

    favorites = relationship('Favorite', back_populates='character')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)

    user = relationship('User', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')

render_er(Base, 'diagram.png')
