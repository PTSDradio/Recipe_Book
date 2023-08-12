# from sqlalchemy import func
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

engine = create_engine('sqlite:///recipe.db')
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    genre = Column(String())
    time = Column(String())
    instructions = Column(String())
    
    # user_id = Column(Integer(), ForeignKey("users.id"))
    ing = relationship('Ingredient', secondary="recipe_ingredients", back_populates='rec')

    user_r = relationship('User', secondary="user_recipe", back_populates='rec_u')

    def __repr__(self):
        return f'Id: {self.id}),' \
            f'Rec Name: {self.name},' \
            f'Rec Genre: {self.genre},' \
            f'Rec Time to Cook: {self.time},' \
            f'Author: {self.user_id},' \
            f'Rec Ingredient ID: {self.ingredient}' \
        

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    password = Column(String())
    # food_restrictions = Column(String())#ARRAY
    rec_u = relationship('Recipe', secondary="user_recipe", back_populates='user_r')

    # recipes = relationship("Recipe", backref="user")
    def __repr__(self):
        return f'Id: {self.id}),' \
            f'User Name: {self.name},' \
            f'User Password: {self.password},' \
            f'User Saved Recipes: {self.saved_recipes}' \
            # f'User Food Restrictions: {self.food_restrictions},' \


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    category = Column(String())#ARRAY

    rec =  relationship('Recipe', secondary="recipe_ingredients", back_populates='ing')
    def __repr__(self):
        return f'Ing Id: {self.id},' \
            f'Ing Name: {self.name},' \
            f'Ing Category: {self.category}' \
            f'ing recipes used: {self.recipe}'
    
            
class RecipeIng(Base):
    __tablename__ = 'recipe_ingredients'

    # id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer(), ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = Column(Integer(), ForeignKey('ingredients.id'), primary_key=True)

    # recipe = relationship('Recipe', back_populates="recipe_ingredients")
    # ingredient = relationship('Ingredient', back_populates="recipe_ingredients")
    
    # def __init__(self, recipe=None, ingredient=None):
    #     self.recipe = recipe
    #     self.ingredient = ingredient

    def __repr__(self):
        return f'Recipe_ingredients(recipe_id={self.recipe_id},' \
            f'ingredient_id={self.ingredient_id}' 
    

class UserRec(Base):
    __tablename__ = 'user_recipe'


    recipe_id = Column(Integer(), ForeignKey('recipes.id'), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'), primary_key=True)


    def __repr__(self):
        return f'user_recipe(recipe_id={self.recipe_id},' \
            f'user_id={self.user_id} ' 