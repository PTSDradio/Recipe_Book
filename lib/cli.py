
from sqlalchemy import create_engine, text
from db.models import Base, User, Recipe, Ingredient
from sqlalchemy.orm import sessionmaker, Session
engine = create_engine('sqlite:///recipe.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session =Session()


def main():
    # mock_list_of_recipes= ["recipe 1", "recipe 2", "recipe 3", "recipe 4"]
    query= text('SELECT * FROM recipes')
    mock_list_of_recipes=session.execute(query)
    #mock_list= mock_list_of_recipes.fetchall()
    for row in mock_list_of_recipes:
        print(row)
    choice = 0
    # while choice !=4:
    #     print("***Recipes R Us***")
    #     print("1)Add a Recipe")
    #     print("2) Lookup a Recipe")
    #     print("3) Display Recipe")
    #     print("4) Quit")
    #     choice = int(input())

if __name__ == "__main__":
    main()

