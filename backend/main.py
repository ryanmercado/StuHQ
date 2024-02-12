from flask import Flask, request, jsonify
from recipe import Recipe, GroceryList, Stock, user_events, to_do_list

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


@calendarAPI.route('/api/addTo_ToDoList', methods=['POST'])
def addTo_ToDoList():
    data = request.get_json()
    usr_id = data['usr_id']
    event_desc = data['event_desc']
    event_type = data['event_type']
    event_title = data['event_title']
    start_epoch = data['start_epoch']
    end_epoch = data['end_epoch']
    return to_do_list.add_to_list(usr_id, event_desc, event_type, event_title, start_epoch, end_epoch)


@calendarAPI.route('/api/getToDoList', methods=['GET'])
def get_ToDoList():
    data = request.get_json()
    usr_id = data['usr_id']
    return to_do_list.get_todo_list(usr_id)


@calendarAPI.route('/api/createEvent', methods=['POST']) 
def createEvent():
    data = request.get_json()
    usr_id = data['usr_id']
    event_desc = data['event_desc']
    event_type = data['event_type']
    event_title = data['event_title']
    start_epoch = data['start_epoch']
    end_epoch = data['end_epoch']
    on_to_do_list = data['on_to_do_list']
    extra_data = data['extra_data']
    is_submitted = data['is_submitted']
    want_notification = data['want_notification']
    return user_events.create_event(usr_id, event_desc, event_type, event_title, start_epoch, end_epoch, on_to_do_list, extra_data, is_submitted, want_notification)


@calendarAPI.route('/api/getEventInformation', methods=['GET']) 
def getEventInformation():
    data = request.get_json()
    event_id = data['event_id']
    return user_events.get_event(event_id)


@calendarAPI.route('/api/getUserEvents', methods=['GET']) 
def getUserEvents():
    data = request.get_json()
    usr_id = data['usr_id']
    return user_events.get_usr_events(usr_id)


@calendarAPI.route('/api/updateEvent', methods=['POST']) 
def updateEvent():
    data = request.get_json()
    event_id = data['event_id']
    event_desc = data['event_desc']
    event_type = data['event_type']
    event_title = data['event_title']
    start_epoch = data['start_epoch']
    end_epoch = data['end_epoch']
    on_to_do_list = data['on_to_do_list']
    extra_data = data['extra_data']
    is_submitted = data['is_submitted']
    want_notification = data['want_notification']
    return user_events.update_event(event_id, event_title, event_desc, event_type, start_epoch, end_epoch, on_to_do_list, extra_data, is_submitted, want_notification) 


@calendarAPI.route('/api/deleteEvent', methods=['POST']) 
def deleteEvent():
    data = request.get_json()
    event_id = data['event_id']
    return user_events.delte_event(event_id)



if __name__ == '__main__':
    recipeAPI.run(debug=True)

