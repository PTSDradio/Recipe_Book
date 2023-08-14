from db.models import User, Ingredient, Recipe, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session =Session()



user=None

log_in = False


def main():

    


    choice = 0
    while choice !=4:
        print("***Recipes R Us***")
        print("1) Account")
        print("2) Lookup a Recipe")
        print("3) Display All Recipes'")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("running account")
            account()

            


        if choice == 2:
            preference = 0
            while preference != 5:
                print("What woult you like to search via?")
                print("1) Name")
                print("2) Genre")
                print("3) Ingredient")
                print("4) Region...Grant :D")
                print("5) Return")
                preference = int(input())

                if preference == 1:
                    print("Search via name")
                    keyword = input("Search here: ")
                    filterRecipeByName(keyword)

                elif preference == 2:
                    print("Search via Genre")
                    keyword = input("Search here: ")
                    filterRecipeByGenre(keyword)
                
                elif preference == 3:
                    print("Search via Ingredient")
                    keyword = input("Search here: ")
                    filterRecipeByIng(keyword)
                
                elif preference == 4:
                    print("...Detriot")
            

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

def account():
    if log_in is False:
        opt = 0
        while opt != 3:
            print("1) Login")
            print("2) Create account")
            opt = int(input())
            if opt == 1:
                print("i worked")
                tex = input("name:")
                mex = input("password:")
                login(tex, mex)
                opt = 3
            elif opt ==2:
                create_user()
                opt = 3


    elif log_in is True:
        opt = 0
        while opt != 3:
            print("1) View your favorites")
            print("2) Remove a recipe from your favorites")
            print("3) Nvm")
            opt = int(input())
            if opt == 1:
                view_favorites()
                opt = 3
            elif opt == 2:
                remove_favorite()
                opt = 3

def show_recipe(recipe):

    print('{:*^80}'.format(f'{recipe.name}'))
    print(f"Genres:{recipe.genre}")
    print('{:-^80}'.format('Ingredients'))
    for ing in recipe.ing:
        print(ing.name)
    # print(f'{recipe.ing}')
    print('{:-^80}'.format('Instructions'))
    print(recipe.instructions)        

def login(username, password):
    acc = session.query(User).filter(User.name == username, User.password == password).first()
    if acc!= None and acc.name == username and acc.password == password:
        global user
        user = session.query(User).filter(User.name == username, User.password == password).first()
        global log_in
        log_in= True
        print(f"Welcome {user.name}!")

    else:
        print("Login failed: Either username or password is incorrect")
    # for user in account:
    #     if user.name == username

def create_user():
    global user
    global log_in
    new_nombre = input("Create a username: ")
    new_passw = input("Create a password: ")
    new_user = User(name=new_nombre, password=new_passw)
    session.add(new_user)
    session.commit()
    
    user = session.query(User).filter(User.name == new_nombre, User.password == new_passw).first()
    log_in = True
    print(f"Welcome {new_nombre}!")

def view_favorites():

    if user.rec_u:
        for rec in user.rec_u:
            print(rec.name)
        inp = input("Type in the recipe name you want to show:")
        for rec in user.rec_u:
            if rec.name == inp:
                show_recipe(rec)
    else:
        print("you have no favorites silly!")

def remove_favorite():
    global user
    if user.rec_u:
        for rec in user.rec_u:
            print(rec.name)
        inp = input("Type in the recipe name you want to show:")
        for rec in user.rec_u:
            if rec.name == inp:
                user.rec_u.remove(rec)
                session.commit()
                print(f"{inp} successfully removed from favs")
            else:
                print(f"{inp} is not in your favs")
    else:
        print("you have no favorites to remove silly!")

# def filterIngredientsByCategory(cat):

#     query= text('SELECT * FROM ingredients WHERE category='+cat)
#     recipes=session.execute(query)
#     statement=''
#     for row in recipes:
#         statement += row
#     return statement

def filterRecipeByName(search):
    global user
    global log_in
    print("***Results!***")
    query = session.query(Recipe).filter(Recipe.name.like(f'%{search}%'))
    print()
    if query.count() > 0:
        for row in query:
            print(row.name)
        selector = input("Select a recipe:")
        for row in query:
            if row.name == selector:
                show_recipe(row)
                if log_in == True:
                    k = input("add favorite y/n?:")
                    if k == "y" or "yes":
                        user.rec_u.append(row)
                        session.commit()
                        print(f"{row.name} added to favorites")
    else:
        print("no recipes include that bruv")


def filterRecipeByGenre(genre):
    global user
    global log_in
    print("***Results!***")
    query = session.query(Recipe).filter(Recipe.genre.like(f'%{genre}%'))
    print()
    if query.count() > 0:
        for row in query:
            print(row.name)
        selector = input("Select a recipe:")
        for row in query:
            if row.name == selector:
                show_recipe(row)
                if log_in == True:
                    k = input("add favorite y/n?:")
                    if k == "y" or "yes":
                        user.rec_u.append(row)
                        session.commit()
                        print(f"{row.name} added to favorites")
    else:
        print("no recipes include that bruv")


def filterRecipeByIng(search):
    global user
    global log_in
    print("***Results!***")
    query = session.query(Ingredient).filter(Ingredient.name.like(f'%{search}%'))

    print()
    if query.count() > 0:
        for row in query:
            print(row.name)
        selector = input("Select the Ingredient: ")
        for row in query:
            if row.name == selector:
                for rec in row.rec:
                    print(rec.name)
                selector = input("Select a recipe:")
                for rec in row.rec:
                    if rec.name == selector:
                        show_recipe(rec)
                        if log_in == True:
                            k = input("add favorite y/n?:")
                            if k == "y" or "yes":
                                user.rec_u.append(rec)
                                session.commit()
                                print(f"{rec.name} added to favorites")
                          

                
                # if log_in == True:
                #     k = input("add favorite y/n?:")
                #     if k == "y" or "yes":
                #         user.rec_u.append(rec)
                #         session.commit()
                #         print(f"{rec.name} added to favorites")
    else:
        print("no recipes include that bruv")









