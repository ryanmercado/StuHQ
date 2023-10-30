from flask import Flask, request, jsonfiy
from recipeToList import RecipeBook, GroceryList

recipeAPI = Flask(__name__)

recipeBook = RecipeBook.RecipeBook()
groceryList = GroceryList.GroceryList()


@recipeAPI.route('/api/addRecipe', methods=['POST'])
def create_recipe():
    data = request.get_json()
    name = data['name']
    ingredients = data['ingredients']

    recipe = RecipeBook.Recipe(name, ingredients)
    recipeBook.add_recipe(recipe)
    return jsonify({'message': 'Recipe created successfully'})


@recipeAPI.route('/api/removeRecipe', methods=['POST'])
def delete_recipe():
    data = request.get_json()
    name = data['name']
    ingredients = data['ingredients']

    recipe = RecipeBook.Recipe(name, ingredients)
    recipeBook.remove_recipe(recipe)
    return jsonify({'message': 'Recipe deleted successfully'})


@recipeAPI.route('/api/getRecipes', methods=['GET'])
def get_recipes():
    recipes = recipeBook.get_recipes()
    recipe_data = [{'name': recipe.get_name(), 'ingredients': recipe.get_ingredients()} for recipe in recipes]
    return jsonify(recipe_data)


@recipeAPI.route('/api/addIngredient', methods=['POST'])
def add_ingredient():
    data = request.get_json()
    ingredient = data['ingredient']

    groceryList.add_item(ingredient)
    return jsonify({'message': 'Ingredient added successfully'})


@recipeAPI.route('/api/removeIngredient', methods=['POST'])
def remove_ingredient():
    data = request.get_json()
    ingredient = data['ingredient']

    groceryList.remove_item(ingredient)
    return jsonify({'message': 'Ingredient deleted successfully'})


@recipeAPI.route('/api/addRecipeIngredients', methods=['POST'])
def add_recipe_ingredients():
    data = request.get_json()
    name = data['name']
    ingredients = data['ingredients']

    recipe = RecipeBook.Recipe(name, ingredients)

    groceryList.add_recipe_ingredients(recipe)
    return jsonify({'message': 'Ingredients added successfully'})


if __name__ == '__main__':
    recipeAPI.run(debug=True)
