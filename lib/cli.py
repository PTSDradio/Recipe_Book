
from sqlalchemy import create_engine, text
from db.models import Base, User, Recipe, Ingredient
from sqlalchemy.orm import sessionmaker, Session
from functions import main
# engine = create_engine('sqlite:///recipe.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session =Session()

if __name__ == "__main__":

    main()

