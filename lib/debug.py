import ipdb
from user import User
from recipe import Recipe
from ingredient import Ingredient


if __name__ == "__main__":


    cherry = Ingredient("cherry", "fruit")
    ribeye = Ingredient("ribeye", "beef")
    eggplant = Ingredient("eggplant", "vegetable")
    skirtsteak = Ingredient("skirtsteak", "beef")
    nystrip = Ingredient("nystrip", "beef")
    halibut = Ingredient("halibut", "fish")
    milk = Ingredient("milk", "dairy")
    egg = Ingredient("egg", "eggs")
    ryebread = Ingredient("ryebread", "bread")
    broccoli = Ingredient("broccoli", "vegetable")

    fritata = Recipe("fritata", [cherry,ribeye,eggplant,skirtsteak,nystrip,halibut,milk,egg,ryebread])
    gfrecipe = Recipe("gfrecipe", [cherry, eggplant, broccoli])
    meat = Recipe("meat", [ribeye, nystrip, skirtsteak])


    fritata.restrictions(["beef", "fish"])
    print("welcome")

    # ipdb.set_trace()