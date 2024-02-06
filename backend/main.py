from flask import Flask, request, jsonify
from recipe import Recipe, GroceryList, Stock

recipeAPI = Flask(__name__)

@recipeAPI.route('/api/addRecipe', methods=['POST'])
def create_recipe():
    data = request.get_json()
    usr_id = data['usr_id']
    name = data['name']
    ingredients = data['ingredients']
    measurements = data['measurements']
    steps = data['steps']

    recipe = Recipe.Recipe(name, ingredients,measurements, steps)
    recipes = [recipe]
    Recipe.addRecipe(usr_id, recipes)
    return jsonify({'message': 'Recipe created successfully'})


@recipeAPI.route('/api/removeRecipe', methods=['POST'])
def delete_recipe():
    data = request.get_json()
    usr_id = data['usr_id']
    name = data['name']
    
    Recipe.removeRecipe(usr_id, name)
    return jsonify({'message': 'Recipe deleted successfully'})


@recipeAPI.route('/api/getRecipes', methods=['GET'])
def get_recipes():
    data = request.get_json()
    usr_id = data['usr_id']
    return Recipe.getRecipes(usr_id)
    


@recipeAPI.route('/api/addGroceryListIngredient', methods=['POST'])
def add_ingredient():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']

    GroceryList.add_item(usr_id, item)
    return jsonify({'message': 'Ingredient added successfully'})


@recipeAPI.route('/api/removeGroceryListIngredient', methods=['POST'])
def remove_ingredient():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']

    GroceryList.delete_item(usr_id,item)
    return jsonify({'message': 'Ingredient deleted successfully'})


@recipeAPI.route('/api/getGroceryList', methods=['GET'])
def getGroceryList():
    data = request.get_json()
    usr_id = data['usr_id']

    return GroceryList.get_items(usr_id)


@recipeAPI.route('/api/addStockItem', methods=['POST'])
def addStockItem():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']
    Stock.add_item(usr_id, item)
    return jsonify({'message': 'Item added successfully'})


@recipeAPI.route('/api/removeStockItem', methods=['POST'])
def removeStockItem():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']  
    Stock.delete_item(usr_id, item)
    return jsonify({'message': 'Item removed successfully'})


@recipeAPI.route('/api/getStock', methods=['GET'])
def getStockItems():
    data = request.get_json()
    usr_id = data['usr_id']
    return Stock.get_items(usr_id)

if __name__ == '__main__':
    recipeAPI.run(debug=True)
