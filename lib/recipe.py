



class Recipe:
    all = []
    def __init__(self, name, ingredients=[], genre=None, instructions=None):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.genre = genre
        Recipe.all.append(self)
    def add_ingred(self, ing):
        self.ingredients.append(ing)

    def displayAll(self):
        pass

    def displayOneByOne(self):
        pass

    @classmethod
    def filterByIngredients(cls, foods, ingredient):
        filt=[]
        for food in foods:
            if isinstance(food, Recipe):
                if ingredient in food.ingredients:
                    filt.append(food)
        return filt
    
    @classmethod
    def filterByIngredientsAndCategory(cls, foods, ingredient, category):
        filt=[]
        for food in foods:
            if isinstance(food, Recipe):

                if ingredient in food.ingredients:
                    filt.append(food)
        return  filt   
    
    # @classmethod
    # def filterByFoodRestrictions(cls, foods, restrictions):
        # filt=[]
        # print(foods)
        # print(restrictions)
        # for food in foods:
        #     if isinstance(food, Recipe):
        #         if restrictions[1] is "GF":
        #             g_count=0
        #             if restrictions[0] is "vegetarian":
        #                 nonvegetarian_count=0
        #                 from ingredient import Ingredient
                                       
        #                 for ingred in food.ingredients:
        #                     if isinstance(ingred,Ingredient):
        #                         print(ingred.category)
        #                         if ingred.category[1] is "contains gluten":
        #                             g_count +=1
        #                         if ingred.category[0] is "meat" or ingred.category[0] is "fish":
        #                             nonvegetarian_count +=1
        #                 print(g_count, nonvegetarian_count)
        #                 if g_count is 0 and nonvegetarian_count is 0:
        #                     filt.append(food)
        #             elif restrictions[0] is "vegan":
        #                 nonvegan_count=0
        #                 from ingredient import Ingredient
                                       
        #                 for ingred in food.ingredients:
        #                     if isinstance(ingred,Ingredient):
        #                         if ingred.category[1] is "contains gluten":
        #                             g_count +=1
        #                         if ingred.category[0] is "meat" or ingred.category[0] is "fish" or ingred.category[0] is "dairy":
        #                             nonvegan_count +=1
        #                 if g_count is 0 and nonvegan_count:
        #                     filt.append(food)
        #             elif restrictions[0] is "pescatarian":
        #                 m_count=0
        #                 from ingredient import Ingredient
                                       
        #                 for ingred in food.ingredients:
        #                     if isinstance(ingred,Ingredient):
        #                         if ingred.category[1] is "contains gluten":
        #                             g_count +=1
        #                         if ingred.category[0] is "meat":
        #                             m_count +=1
        #                 if g_count is 0 and m_count:
        #                     filt.append(food)
        #             else:
        #                 from ingredient import Ingredient
                                       
        #                 for ingred in food.ingredients:
        #                     if isinstance(ingred,Ingredient):
        #                         if ingred.category[1] is "contains gluten":
        #                             g_count +=1
        #                     if g_count is 0:
        #                         filt.append(food)
        #         elif restrictions[1] is None:
        #             if restrictions[0] is "vegetarian":
        #                 nonvegetarian_count=0
        #                 from ingredient import Ingredient
                                       
        #                 for ingred in food.ingredients:
        #                     if isinstance(ingred,Ingredient):
        #                         if ingred.category[0] is "meat" or ingred.category[0] is "fish":
        #                             nonvegetarian_count +=1
        #                 if nonvegetarian_count is 0:
        #                     filt.append(food)
        #             elif restrictions[0] is "vegan":
        #                 nonvegan_count=0
        #                 from ingredient import Ingredient
                                       
        #                 for ingred in food.ingredients:
                            
        #                         if ingred.category[0] is "meat" or ingred.category[0] is "fish" or ingred.category[0] is "dairy":
        #                             nonvegan_count +=1
        #                 if nonvegan_count:
        #                     filt.append(food)
        #             elif restrictions[0] is "pescatarian":
        #                 m_count=0
        #                 from ingredient import Ingredient                                   
        #                 for ingred in food.ingredients:
        #                     if isinstance(ingred,Ingredient):
        #                         if ingred.category[0] is "meat":
        #                             m_count +=1
        #                 if  m_count:
        #                     filt.append(food)
        #         print("success")
        # return  filt  
    
    vegetarian =["beef", "fish"]
    vegan =[]
    pescatarian =[]

    @classmethod
    def restrictions(cls, restriction):
        results = []
        for recipe in cls.all:
            stat = True
            for ingred in recipe.ingredients:
                if ingred.category not in restriction:
                    stat = False
            if stat == True and not recipe in results:
                results.append(recipe)
        print (results)
        pass

            



