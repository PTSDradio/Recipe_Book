# from sqlalchemy import func
from sqlalchemy import create_engine, Column, Integer, String, DateTime 
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///recipe.db')

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    genre = Column(String())
    time = Column(String())
    
    # users = relationship('User')
    # ingredients = relationship('Ingredient')

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    password = Column(String())
    food_restrictions = Column(String())
    saved_recipes = Column(String())


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    category = Column(String())

    # recipe used in
    # recipe = relationship()