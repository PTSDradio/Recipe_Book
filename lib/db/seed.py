from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine('sqlite:///recipe.db')
session = Session(engine, future=True)