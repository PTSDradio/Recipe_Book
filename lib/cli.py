
from sqlalchemy import create_engine, text
from db.models import Base, User, Recipe, Ingredient
from sqlalchemy.orm import sessionmaker, Session
engine = create_engine('sqlite:///recipe.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session =Session()
user=None

def main():
    choice = 0
    while choice !=4:
        print("***Recipes R Us***")
        print("1)Add a Recipe")
        print("2) Lookup a Recipe")
        print("3) Display All Recipes'")
        print("4) Quit")
        choice = int(input())

        if choice == 2:
            preference = 0
            print("What woult you like to search via?")
            print("1)Name")
            print("2)Genre")
            print("3)Ingredients")
            # print("4)Author")
            print("5)Return")
            print("6)Region")
            preference = int(input())

            if preference == 1:
                print("Search via name")
                keyword = input("Search here: ")
                filterRecipeByName(keyword)

            elif preference == 2:
                print("Search via Genre")
                keyword = input("Search here: ")
                filterRecipeByGenre(keyword)
            
            elif preference == 5:
                main()
            

        elif choice == 3:
            print("As you wish...")
            show_all_recipes()

def show_all_recipes():
        # mock_list_of_recipes= ["recipe 1", "recipe 2", "recipe 3", "recipe 4"]
    query= text('SELECT * FROM recipes')
    mock_list_of_recipes=session.execute(query)
    #mock_list= mock_list_of_recipes.fetchall()
    numbering= 0
    for row in mock_list_of_recipes:
        numbering+=1
        print(f'{numbering}){row.name}')

# def filterIngredientsByCategory(cat):

#     query= text('SELECT * FROM ingredients WHERE category='+cat)
#     recipes=session.execute(query)
#     statement=''
#     for row in recipes:
#         statement += row
#     return statement

def filterRecipeByGenre(genre):
    print("***Results!***")
    query = session.query(Recipe).filter(Recipe.genre.like(f'%{genre}%'))
    
    for row in query:
        print(row.name)
    selector = input("Select a recipe:")
    for row in query:
        if row.name == selector:
            show_recipe(row)

def filterRecipeByName(search):
    # query= text(f'SELECT * FROM recipes WHERE name= ?')
    # recipes=session.execute(query)
    print("***Results!***")
    query = session.query(Recipe).filter(Recipe.name.like(f'%{search}%'))
    
    for row in query:
        print(row.name)
    selector = input("Select a recipe:")
    for row in query:
        if row.name == selector:
            show_recipe(row)


# def grab_item_by_id(cls, id):
#     session.query(cls).filter(Recipe.id == id)
#     pass

def show_recipe(recipe):

    
    print('{:*^20}'.format(f'{recipe.name}'))
    print(f"Genres:{recipe.genre}")
    print('{:-^20}'.format('Ingredients'))
    for ing in recipe.ing:
        print(ing.name)
    # print(f'{recipe.ing}')
    print('{:-^20}'.format('Instructions'))
    print(recipe.instructions)

# def filterRecipeByAuthor():
#     query= text('SELECT * FROM recipes WHERE user_id='+user)
#     recipes=session.execute(query)
#     statement=''
#     for row in recipes:
#         statement += row
#     return statement

# def filterRecipeByIngredients(ingredients):
#     pass

# def displayRecipeIngredients(recipe_id):
#     pass

# def addRecipe():
#     pass

# def login(username, password):
#     query= text('SELECT id FROM users WHERE name=username and password='+password)
#     recipes=session.execute(query)
#     statement=''
#     for row in recipes:
#         statement += row
#     return statement

if __name__ == "__main__":
    main()

