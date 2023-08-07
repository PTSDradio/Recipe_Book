



class Ingredient:
    all = []
    def __init__(self, name, category=None):
        self.name = name
        self.category = category
        Ingredient.all.append(self)