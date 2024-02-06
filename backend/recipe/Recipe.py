import sqlite3
import json
from flask import jsonify

class Recipe:
    ingredients = []
    measurements = []
    name = ''
    steps = ''

    def __init__(self, name, ingredients, measurements, steps):
        self.name = name
        self.ingredients = ingredients
        self.measurements = measurements
        self.steps = steps

    def addRecipe(id, recipes):

        #precondtion: id is an int, recipes is a list of Recipe objects
        #postcondition: adds recipe list to users(id) current list

        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(*) FROM recipes WHERE usr_id = ?', (id,))
        result = cursor.fetchone()
        id_exists = result[0] > 0

        if id_exists:

            cursor.execute("SELECT recipe_lists FROM recipes WHERE usr_id = ?", (id,))
            result = cursor.fetchone()
            current_recipes_json = result[0] if result else '[]'
            current_recipes = json.loads(current_recipes_json)
            recipe_exists = False
            for rec in current_recipes:
                if rec['name'] == recipes[0].name:
                    recipe_exists = True

            if not recipe_exists:
                current_recipes.extend(recipes)

            updated_recipes_json = json.dumps(current_recipes, cls=RecipeEncoder)
            cursor.execute('UPDATE recipes SET recipe_lists = ? WHERE usr_id = ?', (updated_recipes_json, id))
        
        else:
            recipes_json = json.dumps(recipes, cls=RecipeEncoder)
            cursor.execute('INSERT INTO recipes (usr_id, recipe_lists) VALUES (?, ?)', (id, recipes_json))

        conn.commit()
        cursor.close()
        conn.close()
    
    def removeRecipe(id, name): 
        
        #precondition: id is an int, name is a string 
        #postcondition: removes the specified recipe if it exists

        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM recipes WHERE id = ?', (id,))
        result = cursor.fetchone()
        id_exists = result[0] > 0
        if id_exists:

            cursor.execute("SELECT recipe_lists from recipes WHERE usr_id = ?", (id,))
            result = cursor.fetchone()
            current_recipes_json = result[0] if result else '[]'
            current_recipes = json.loads(current_recipes_json)
            new_recipes = []
            for recipe in current_recipes:
                if recipe['name'] == name:
                    continue
                else:
                    new_recipes.append(recipe)

            updated_recipes_json = json.dumps(new_recipes, cls=RecipeEncoder)
            cursor.execute('UPDATE recipes SET recipe_lists = ? WHERE usr_id = ?', (updated_recipes_json, id))

        conn.commit()
        cursor.close()
        conn.close()

    def getRecipes(id):

        #precondition: id must be an int (does not have to exist, there are check)
        #postcondition: returns json formatted list of all recipes associated with the id

        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM recipes WHERE usr_id = ?', (id,))
        result = cursor.fetchone()
        id_exists = result[0] > 0
        if id_exists:
            cursor.execute("SELECT recipe_lists FROM recipes WHERE usr_id = ?", (id,))
            result = cursor.fetchone()
            current_recipes_json = result[0] if result else '[]'
            conn.close()
            cursor.close()
            return current_recipes_json
        conn.close()
        cursor.close()
        return jsonify({'result': 'id did not exist'})

        


class RecipeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Recipe):
            return {
                'name': obj.name,
                'ingredients': obj.ingredients,
                'measurements': obj.measurements,
                'steps': obj.steps
            }
        return json.JSONEncoder.default(self, obj)
    


#SAMPLE
# recipe = Recipe(
#     name='Luke',
#     ingredients=['dough', 'tomato sauce', 'cheese'],
#     measurements = [(300, 'g'), (200, 'g'), (200, 'g')],
#     steps='Cook dough, add sauce and cheese'
# )
# recipes = [recipe]

# Recipe.addRecipe(0, recipes)
# Recipe.removeRecipe(0, 'Gerber')
