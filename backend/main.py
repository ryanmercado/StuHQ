from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from recipe import Recipe, GroceryList, Stock
from calendar_module import user_events, to_do_list
from resume.Resume import Resume
from resume.generateResume import generateResume, deleteResumeFile
import handleCreateAccount, handleSignIn
import os
import time


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

    recipe = Recipe.Recipe(name, ingredients, measurements, steps)
    recipes = [recipe]
    Recipe.Recipe.addRecipe(usr_id, recipes)
    return jsonify({'message': 'Recipe created successfully'})


@stuAPI.route('/api/removeRecipe', methods=['POST'])
def delete_recipe():
    data = request.get_json()
    usr_id = data['usr_id']
    name = data['name']
    
    Recipe.Recipe.removeRecipe(usr_id, name)
    return jsonify({'message': 'Recipe deleted successfully'})


@stuAPI.route('/api/getRecipes', methods=['GET'])
def get_recipes():
    usr_id = request.args.get('usr_id')
    return Recipe.Recipe.getRecipes(usr_id)


@stuAPI.route('/api/purchasedIngredient', methods=['POST'])
def purchase_item():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']

    GroceryList.GroceryList.purchased_item(usr_id, item)
    return jsonify({'message': 'done'})


@stuAPI.route('/api/addGroceryListIngredient', methods=['POST'])
def add_ingredient():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']
    
    GroceryList.GroceryList.add_item(usr_id, item)
    return jsonify({'message': 'Ingredient added successfully'})


@stuAPI.route('/api/removeGroceryListIngredient', methods=['POST'])
def remove_ingredient():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']

    GroceryList.GroceryList.delete_item(usr_id, item)
    return jsonify({'message': 'Ingredient deleted successfully'})


@stuAPI.route('/api/getGroceryList', methods=['GET'])
def getGroceryList():
    usr_id = request.args.get('usr_id')
    return GroceryList.GroceryList.get_items(usr_id)


@stuAPI.route('/api/addStockItem', methods=['POST'])
def addStockItem():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']
    Stock.Stock.add_item(usr_id, item)
    return jsonify({'message': 'Item added successfully'})


@stuAPI.route('/api/removeStockItem', methods=['POST'])
def removeStockItem():
    data = request.get_json()
    usr_id = data['usr_id']
    item = data['item']  
    Stock.Stock.delete_item(usr_id, item)
    return jsonify({'message': 'Item removed successfully'})


@stuAPI.route('/api/getStock', methods=['GET'])
def getStockItems():
    usr_id = request.args.get('usr_id')
    return Stock.Stock.get_items(usr_id)

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
    event_id = request.args.get('event_id')
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

@stuAPI.route('/api/addResumeExperience', methods=['POST'])
def add_resume_experience():
    try:
        resume = Resume()  # Assuming Resume class is imported or defined
        data = request.get_json()
        user_id = data.get('user_id')
        company = data.get('company')
        role = data.get('role')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        location = data.get('location')
        desc_arr = data.get('desc_arr')

        if not all([user_id, company, role, start_date, end_date, location, desc_arr]):
            return jsonify({'error': 'Missing required fields'}), 400

        resume.addExperience(user_id, company, role, start_date, end_date, location, desc_arr)
        return jsonify({'message': 'Experience added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@stuAPI.route('/api/addResumeExtracurr', methods=['POST'])
def addResumeExtracurr():
    try:
        resume = Resume()
        data = request.get_json()
        user_id = data.get('user_id')
        title = data.get('title')
        desc = data.get('desc')

        # Check if all required fields are present in the request
        if not all([user_id, title, desc]):
            return jsonify({'error': 'Missing required fields: ()'}), 400

        # Call the addExtracurr method with the provided data
        resume.addExtracurr(user_id, title, desc)

        # Return success response
        return jsonify({'message': 'Extracurricular added successfully'}), 200

    except KeyError as e:
        # Handle case where required fields are missing from the request
        return jsonify({'error': f'Missing required field: {e}'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500
        # Handle other exceptions


@stuAPI.route('/api/addResumeGeneralInfo', methods=['POST'])
def addResumeGeneralInfo():
    try:
        # Assuming Resume() and resume.addGeneralInfo() work as expected
        resume = Resume()
        
        # Get JSON data from request
        data = request.get_json()
        
        # Extract data from JSON
        user_id = data.get('user_id')
        lastname = data.get('lastname')
        firstname = data.get('firstname')
        phone = data.get('phone')
        email = data.get('email')
        linkedin = data.get('linkedin')
        edu = data.get('edu')
        grad_date = data.get('grad_date')
        major = data.get('major')
        GPA = data.get('GPA')
        
        # Check if all required fields are present
        if None in [user_id, lastname, firstname, phone, email, linkedin, edu, grad_date, major, GPA]:
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Call method to add general info to resume
        resume.addGeneralInfo(user_id, lastname, firstname, phone, email, linkedin, edu, grad_date, major, GPA)
        
        # Return success response
        return jsonify({'message': 'General info added successfully'}), 200
    except KeyError as e:
        # Handle KeyError if any required field is missing from the JSON data
        return jsonify({'error': f'Missing field: {e.args[0]}'}, 400)
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': str(e)}), 500

@stuAPI.route('/api/addResumeTechnicalSkill', methods=['POST'])
def addResumeTechnicalSkill():
    try:
        resume = Resume()
        data = request.get_json()
        user_id = data['user_id']
        name = data['name']
        resume.addTechnicalSkill(user_id, name)
        return jsonify({'success': True}), 200
    except KeyError as e:
        # Handle KeyError if 'user_id' or 'name' is missing in the request JSON
        return jsonify({'error': f'Missing required field: {e}'}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500



@stuAPI.route('/api/addResumeProject', methods=['POST'])
def addResumeProject():
    try:
        resume = Resume()  # Assuming Resume class is imported or defined
        data = request.get_json()
        user_id = data.get('user_id')
        title = data.get('title')
        who_for = data.get('who_for')
        date = data.get('date')
        desc_arr = data.get('desc_arr')

        if not all([user_id, title, who_for, date, desc_arr]):
            return jsonify({'error': 'Missing required fields'}), 400

        resume.addProject(user_id, title, who_for, date, desc_arr)
        return jsonify({'message': 'Project added successfully'}), 200
    except KeyError as e:
        return jsonify({'error': 'KeyError - Missing required fields: {}'.format(str(e))}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@stuAPI.route('/api/addResumeAward', methods=['POST'])
def addResumeAward():
    resume = Resume()
    data = request.get_json()
    user_id = data['user_id']
    title = data['title']
    desc = data['desc']
    resume.addAward(user_id, title, desc)


@stuAPI.route('/api/addResumeCourse', methods=['POST'])
def addResumeCourse():
    resume = Resume()
    data = request.get_json()
    user_id = data['user_id']
    name = data['name']
    resume.addCourse(user_id, name)


@stuAPI.route('/api/addResumeObjective', methods=['POST'])
def addResumeObjective():
    resume = Resume()
    data = request.get_json()
    user_id = data['user_id']
    obj_string = data['obj_string']
    resume.addObjective(user_id, obj_string)


@stuAPI.route('/api/addResumeVolunteerWork', methods=['POST'])
def addResumeVolunteerWork():
    resume = Resume()
    data = request.get_json()
    user_id = data['user_id']
    company = data['company']
    role = data['role']
    start_date = data['start_date']
    end_date = data['end_date']
    resume.addVolunteerWork(user_id, company, role, start_date, end_date)

@stuAPI.route('/api/deleteResume', methods=['POST'])
def deleteResume():
    resume = Resume()
    data = request.get_json()
    user_id = data['user_id']
    try:
        resume.deleteUserInfo(user_id)
        return jsonify({'message': 'Resume deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@stuAPI.route('/api/generate_resume', methods = ['POST'])
def getResume():
    data = request.get_json()
    user_id = data['user_id']
    try:
        generateResume(user_id)
        pdf_path = f"resumes/resume-{user_id}.pdf" 
        current_directory = os.getcwd()
        new_pdf_path = f"backend/resumes/resume-{user_id}.pdf" 

        os_path =os.path.join(current_directory, new_pdf_path)
        
        while not os.path.exists(os_path):
            time.sleep(1)

        # Check if the file exists before sending it
        if os.path.exists(os_path):
            returner = send_file(pdf_path, as_attachment=True)
            deleteResumeFile(os_path)
            return returner
        else:
            return "Resume not found. at path: " + os_path
    except Exception as e:
        print(e)
        return str(e)





if __name__ == '__main__':
    stuAPI.run()

