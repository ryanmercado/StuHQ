class GroceryList:
    items = []

    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_items(self):
        return self.items

    def add_recipe_ingredients(self, recipe):
        for ingredient in recipe.get_ingredients():
            if ingredient not in self.get_items():
                self.add_item(ingredient)
