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

    followers = relationship('Follower', back_populates='user_to', foreign_keys='Follower.user_to_id')
    following = relationship('Follower', back_populates='user_from', foreign_keys='Follower.user_from_id')
    posts = relationship('Post', back_populates='user')
    comments = relationship('Comment', back_populates='author')
    favorites = relationship('Favorite', back_populates='user')

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)

    user_from = relationship('User', back_populates='following', foreign_keys=[user_from_id])
    user_to = relationship('User', back_populates='followers', foreign_keys=[user_to_id])

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='posts')
    media = relationship('Media', back_populates='post')
    comments = relationship('Comment', back_populates='post')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    url = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

    post = relationship('Post', back_populates='media')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    author = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')

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
