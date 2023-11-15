class GroceryList:
    items = []

    def __init__(self):
        self.items = []

    def add_item(self, item, stock): # todo: add stock to method calls
        if item in stock.get_items():
            return
        if item not in self.items:
            self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_items(self):
        return self.items

    def add_recipe_ingredients(self, recipe, stock):
        for ingredient in recipe.get_ingredients():
            if ingredient in stock.get_items():   # todo: test this
                continue
            if ingredient not in self.get_items():
                self.add_item(ingredient, stock)

    def purchased_item(self, item, stock):
        stock.add_item(item)

    def purchased_items(self, items, stock):
        stock.add_items(items)

