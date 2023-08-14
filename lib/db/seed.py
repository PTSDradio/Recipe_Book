from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from models import (Base, Recipe, Ingredient, User, RecipeIng, UserRec)

if __name__ == "__main__":

    engine =create_engine('sqlite:///recipe.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session =Session()

    session.query(Recipe).delete()
    session.query(Ingredient).delete()
    session.query(User).delete()
    session.query(RecipeIng).delete()
    session.query(UserRec).delete()

    Chili = Recipe(
        name="Chili",
        genre="Soup",
        time="30 Minutes",
        instructions="""
            - Add the olive oil(1 tbsp) to a large soup pot and place it over medium-high heat for two minutes.
              Add the onion(1). Cook for 5 minutes, stirring occasionally.

            - Add the ground beef(1 lbs) to the pot. Break it apart with a wooden spoon.
              Cook for 6-7 minutes, until the beef is browned, stirring occasionally.

            - Add the chili powder(2 1/2 tbsp), cumin(2 tbsp), sugar(2 tbsp), tomato paste(2 tbsp), garlic powder(1 tbsp),
              salt(1 1/2 tsp), pepper(1/2 tsp), and optional cayenne(1/4 tsp). Stir until well combined.

            - Add the broth(1 1/2 cups), diced tomatoes (1 15 oz. can with their juice),
              drained beans(1 16 oz. can), and tomato sauce(1). Stir well.

            - Bring the liquid to a low boil. Then, reduce the heat (low to medium-low) to gently simmer the chili,
              uncovered, for 20-25 minutes, stirring occasionally.

            - Remove the pot from the heat. Let the chili rest for 5-10 minutes before serving.
            """    
    )
    
    olive_oil = Ingredient( name = "olive oil", category = "oil")
    yellow_onion = Ingredient(name = "yellow onion", category = "vegetable")
    ground_beef = Ingredient(name = "ground beef", category = "beef")
    chili_powder = Ingredient(name = "chili_powder", category = "spice")
    ground_cumin = Ingredient(name = "ground_cumin", category = "spice")
    sugar = Ingredient(name = "sugar", category = "sugar")
    tomato_paste = Ingredient(name = "tomato paste", category = "sauce")
    garlic_powder = Ingredient(name = "garlic powder", category = "spice")
    salt = Ingredient(name = "salt", category = "spice")
    black_pepper = Ingredient(name = "black pepper", category = "spice")
    cayenne_pepper = Ingredient(name = "cayenne pepper", category = "spice")
    beef_broth = Ingredient(name = "beef broth", category = "broth")
    tomatoes = Ingredient(name = "tomatoes", category = "vegetable")
    red_kidney_beans = Ingredient(name = "red kidney beans", category = "bean")
    tomato_sauce = Ingredient(name = "tomato sauce", category = "sauce")
    
    chili_ing = [olive_oil, yellow_onion, ground_beef, chili_powder, ground_cumin, sugar, tomato_paste, garlic_powder, salt, black_pepper, cayenne_pepper, beef_broth, tomatoes, red_kidney_beans, tomato_sauce]

    Chili.ing.extend(chili_ing)

    Pancake = Recipe(
        name="Old fashioned Pancakes",
        genre="breakfast, sweets",
        time="20 minutes",
        instructions="""
            - Sift flour(1 1/2 cups), baking powder(3 1/2 tsp), sugar(1 tbsp), and salt(1/4 tsp) together in a large bowl.
              Make a well in the center and add milk(1 1/4 cups), melted butter(3 tbsp), and egg(1); mix until smooth.
            
            - Heat a lightly oiled griddle or pan over medium-high heat. Pour or scoop the batter onto the griddle,
              using approximately 1/4 cup for each pancake; cook until bubbles form and the edges are dry, about 2 to 3 minutes.
              Flip and cook until browned on the other side. Repeat with remaining batter.
            """
    )

    flour = Ingredient(name="flour", category="flour")
    baking_powder = Ingredient(name="baking_powder", category="baking")
    milk = Ingredient(name="milk", category="dairy")
    butter = Ingredient(name="butter", category="dairy")
    egg = Ingredient(name="egg", category="egg")
    pancake_ing = [flour, baking_powder, sugar, salt, milk, butter, egg]
    
    Pancake.ing.extend(pancake_ing)

    user_1 = User( 
        name ="john",
        password ="123"
    )

    user_1.rec_u.append(Chili)

    all_list = chili_ing+[Chili, user_1]

    session.add_all(all_list)
    session.commit()
    # session.commit()