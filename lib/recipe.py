



class Recipe:
    all = []
    def __init__(self, name, ingredients, instructions=None):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        Recipe.all.append(self)