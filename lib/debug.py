




# session = Session(engine, future=True)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from db.models import (Base, Recipe, Ingredient, User)
if __name__ == "__main__":

    engine =create_engine('sqlite:///recipe.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session =Session()
    cherry = Ingredient(name ="cherry", category="fruit")
    ribeye = Ingredient(name ="ribeye", category="beef")
    eggplant = Ingredient(name ="eggplant", category="vegetable")
    skirtsteak = Ingredient(name ="skirtsteak", category="beef")
    nystrip = Ingredient(name ="nystrip", category="beef")
    halibut = Ingredient(name ="halibut", category="fish")
    milk = Ingredient(name ="milk", category="dairy")
    egg = Ingredient(name ="egg", category="eggs")
    ryebread = Ingredient(name ="ryebread", category="bread")
    broccoli = Ingredient(name ="broccoli", category="vegetable")

    fritata = Recipe(name ="fritata", ingredient_id="cherry,ribeye,eggplant,skirtsteak,nystrip,halibut,milk,egg,ryebread", genre = "Mexican", time= "45 minutes", instructions = "blah blah muffin")
    #gfrecipe = Recipe("gfrecipe", [cherry, eggplant, broccoli])
    #meat = Recipe("meat", [ribeye, nystrip, skirtsteak])
    hh=User(name="hh", password="password", food_restrictions="None",saved_recipes="None")
    session.add(cherry)
    session.add(ribeye)
    session.add(eggplant)
    session.add(skirtsteak)
    session.add(nystrip)
    session.add(halibut)
    session.add(milk)
    session.add(egg)
    session.add(ryebread)
    session.add(broccoli)
    session.add(fritata)
    session.add(hh)
    session.execute()
    session.commit()


   # fritata.restrictions(["beef", "fish"])
#    print("welcome")

    # ipdb.set_trace()