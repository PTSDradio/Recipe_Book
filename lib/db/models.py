# from sqlalchemy import func
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///recipe.db').

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer(), primary_key=True)
