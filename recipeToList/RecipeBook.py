class Recipe:
    ingredients = []

    def __init__(self, ingredientList):
        self.ingredients = ingredientList

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

    def add_to_grocery_list(self, groceryList):
        for ingredient in self.ingredients:
            if ingredient not in groceryList.get_items():
                groceryList.add_item(ingredient)

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
