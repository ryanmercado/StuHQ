from flask import Flask, request, jsonify
from flask_cors import CORS
from recipe import Recipe, GroceryList, Stock
from calendar_module import user_events, to_do_list
import handleCreateAccount, handleSignIn


stuAPI = Flask(__name__)
CORS(stuAPI)

@stuAPI.route('/api/addRecipe', methods=['POST'])
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


@stuAPI.route('/api/removeRecipe', methods=['POST'])
def delete_recipe():
    data = request.get_json()
    usr_id = data['usr_id']
    name = data['name']
    
    Recipe.removeRecipe(usr_id, name)
    return jsonify({'message': 'Recipe deleted successfully'})


@stuAPI.route('/api/getRecipes', methods=['GET'])
def get_recipes():
    usr_id = request.args.get('usr_id')
    return Recipe.getRecipes(usr_id)
    


@stuAPI.route('/api/addGroceryListIngredient', methods=['POST'])
def add_ingredient():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']

    GroceryList.add_item(usr_id, item)
    return jsonify({'message': 'Ingredient added successfully'})


@stuAPI.route('/api/removeGroceryListIngredient', methods=['POST'])
def remove_ingredient():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']

    GroceryList.delete_item(usr_id,item)
    return jsonify({'message': 'Ingredient deleted successfully'})


@stuAPI.route('/api/getGroceryList', methods=['GET'])
def getGroceryList():
    usr_id = request.args.get('usr_id')
    return GroceryList.get_items(usr_id)


@stuAPI.route('/api/addStockItem', methods=['POST'])
def addStockItem():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']
    Stock.add_item(usr_id, item)
    return jsonify({'message': 'Item added successfully'})


@stuAPI.route('/api/removeStockItem', methods=['POST'])
def removeStockItem():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']  
    Stock.delete_item(usr_id, item)
    return jsonify({'message': 'Item removed successfully'})


@stuAPI.route('/api/getStock', methods=['GET'])
def getStockItems():
    usr_id = request.args.get('usr_id')
    return Stock.get_items(usr_id)

@stuAPI.route('/api/addTo_ToDoList', methods=['POST'])
def addTo_ToDoList():
    data = request.get_json()
    usr_id = data['usr_id']
    event_desc = data['event_desc']
    event_type = data['event_type']
    event_title = data['event_title']
    start_epoch = data['start_epoch']
    end_epoch = data['end_epoch']
    return to_do_list.add_to_list(usr_id, event_desc, event_type, event_title, start_epoch, end_epoch)


@stuAPI.route('/api/getToDoList', methods=['GET'])
def get_ToDoList():
    data = request.get_json()
    usr_id = data['usr_id']
    return to_do_list.get_todo_list(usr_id)


@stuAPI.route('/api/createEvent', methods=['POST']) 
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
    return user_events.create_event(usr_id=usr_id, event_desc=event_desc, event_type=event_type, event_title=event_title, 
                                    start_epoch=start_epoch, end_epoch=end_epoch, on_to_do_list=on_to_do_list, extra_data=extra_data, 
                                    is_submitted=is_submitted, want_notification=want_notification)

@stuAPI.route('/api/ToDoCreateEvent', methods=['POST']) 
def ToDoCreateEvent():
    data = request.get_json()
    usr_id = data['usr_id']
    event_desc = data['event_desc']
    event_type = data['event_type']
    event_title = data['event_title']
    on_to_do_list = data['on_to_do_list']
    return user_events.create_event(usr_id=usr_id, event_desc=event_desc, event_type=event_type, event_title=event_title, on_to_do_list=on_to_do_list)


@stuAPI.route('/api/getEventInformation', methods=['GET']) 
def getEventInformation():
    data = request.get_json()
    event_id = data['event_id']
    return user_events.get_event(event_id)

@stuAPI.route('/api/getUserEvents', methods=['GET']) 
def getUserEvents():
    usr_id = request.args.get('usr_id')
    return user_events.get_usr_events(usr_id)

@stuAPI.route('/api/updateEvent', methods=['POST']) 
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


@stuAPI.route('/api/toggleToDo', methods=['POST']) 
def toggleToDo():
    print(request.get_json)
    data = request.get_json()
    event_id = data['event_id']
    on_to_do_list = data['on_to_do_list']
    return user_events.toggleToDo(event_id, on_to_do_list)

@stuAPI.route('/api/deleteEvent', methods=['POST']) 
def deleteEvent():
    data = request.get_json()
    event_id = data['event_id']
    return user_events.delete_event(event_id)
 
@stuAPI.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    return handleSignIn.login(username, password)

@stuAPI.route('/api/createAccount', methods=['POST'])
def createAccount():
    data = request.get_json()
    username = data['username']
    password = data['password']
    confirm_password = data['confirm_password']
    email = data['email']
    return handleCreateAccount.sign_up(username, email, password, confirm_password)

if __name__ == '__main__':
    stuAPI.run()

