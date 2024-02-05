from flask import Flask, request, jsonify
from recipe import Recipe, GroceryList, Stock

recipeAPI = Flask(__name__)

recipeBook = RecipeBook.RecipeBook()
groceryList = GroceryList.GroceryList()


@recipeAPI.route('/api/addRecipe', methods=['POST'])
def create_recipe():
    data = request.get_json()
    id = data['id']
    name = data['name']
    ingredients = data['ingredients']
    measurements = data['measurements']
    steps = data['steps']

    recipe = Recipe.Recipe(name, ingredients,measurements, steps)
    recipes = [recipe]
    Recipe.addRecipe(id, recipes)
    return jsonify({'message': 'Recipe created successfully'})


@recipeAPI.route('/api/removeRecipe', methods=['POST'])
def delete_recipe():
    data = request.get_json()
    id = data['id']
    name = data['name']
    ingredients = data['ingredients']
    measurements = data['measurements']
    steps = data['steps']

    recipe = Recipe.Recipe(name, ingredients, measurements, steps)
    name = [recipe]
    Recipe.removeRecipe(id, name)
    return jsonify({'message': 'Recipe deleted successfully'})


@recipeAPI.route('/api/getRecipes', methods=['POST'])
def get_recipes():
    data = request.get_json()
    id = data['id']
    return Recipe.getRecipes(id)
    


@recipeAPI.route('/api/addIngredient', methods=['POST'])
def add_ingredient():
    data = request.get_json()
    id = data['id']
    item = data['item']

    GroceryList.add_item(id, item)
    return jsonify({'message': 'Ingredient added successfully'})


@recipeAPI.route('/api/removeIngredient', methods=['POST'])
def remove_ingredient():
    data = request.get_json()
    id = data['id']
    item = data['item']

    GroceryList.delete_item(id,item)
    return jsonify({'message': 'Ingredient deleted successfully'})


@recipeAPI.route('/api/getGroceryList', methods=['POST'])
def getGroceryList():
    data = request.get_json()
    id = data['id']

    return GroceryList.get_items(id)


@recipeAPI.route('/api/addStockItem', methods=['POST'])
def addStockItem():
    data = request.get_json()
    id = data['id']
    item = data['item']
    Stock.add_item(id, item)
    return jsonify({'message': 'Item added successfully'})


@recipeAPI.route('/api/removeStockItem', methods=['POST'])
def removeStockItem():
    data = request.get_json()
    id = data['id']
    item = data['item']  
    Stock.delete_item(id, item)
    return jsonify({'message': 'Item removed successfully'})


@recipeAPI.route('/api/getStock', methods=['POST'])
def getStockItems():
    data = request.get_json()
    id = data['id']
    return Stock.get_items(id)

if __name__ == '__main__':
    recipeAPI.run(debug=True)
