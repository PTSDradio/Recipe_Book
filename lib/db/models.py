# from sqlalchemy import func
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, ba
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    genre = Column(String())
    time = Column(String())
    
    user_id = Column(Integer(), ForeignKey("users.id"))
    ingredient_id = Column(Integer(), ForeignKey("ingredients.id"))

    def __repr__(self):
        return f'Id: {self.id}),' \
            f'Rec Name: {self.name},' \
            f'Rec Genre: {self.genre},' \
            f'Rec Time to Cook: {self.time},' \
            f'Author: {self.user_id},' \
            f'Rec Ingredient ID: {self.ingredient_id}' \
        

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    password = Column(String())
    food_restrictions = Column(String())#ARRAY
    saved_recipes = Column(String())#array

    recipes = relationship("Recipe", backref="user")
    def __repr__(self):
        return f'Id: {self.id}),' \
            f'User Name: {self.name},' \
            f'User Password: {self.password},' \
            f'User Food Restrictions: {self.food_restrictions},' \
            f'User Saved Recipes: {self.saved_recipes}' \



class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    category = Column(String())#ARRAY

    # recipe
    # recipe = relationship()

    def __repr__(self):
        return f'Ing Id: {self.id},' \
            f'Ing Name: {self.name},' \
            f'Ing Category: {self.category}' \
        