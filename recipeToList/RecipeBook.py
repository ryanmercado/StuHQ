class Recipe:
    ingredients = []
    name = ""

    def __init__(self, name, ingredientList):
        self.ingredients = ingredientList
        self.name = name

    def __eq__(self, recipe):
        for ingredient in self.ingredients:
            if ingredient not in recipe.get_ingredients():
                return False
        for ingredient in recipe.get_ingredients():
            if ingredient not in self.ingredients:
                return False
        return True

    def get_ingredients(self):
        return self.ingredients

    def get_name(self):
        return self.name

    def add_ingredient(self, ingredient):
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)


class RecipeBook:
    recipes = []

    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        if recipe not in self.recipes:
            self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        if recipe in self.recipes:
            self.recipes.remove(recipe)

    def get_recipes(self):
        return self.recipes
