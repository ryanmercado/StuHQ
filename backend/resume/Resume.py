import sqlite3
import json

class Experience:
    def __init__(self, user_id, job_id):
        self.user_id = user_id
        self.job_id = job_id
        self.company = ''
        self.role = ''
        self.start_date = ''
        self.end_date = ''
        self.location = ''
        self.desc_arr = ''

    def setData(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM experience WHERE job_id = ?', (self.job_id,))
        result = cursor.fetchone()

        self.company = result[2]
        self.role = result[3]
        self.start_date = result[4]
        self.end_date = result[5]
        self.location = result[6]
        self.desc_arr = result[7]

        conn.close()

    def getData(self):
        return self.user_id, self.job_id, self.company, self.role, self.start_date, self.end_date, self.location, self.desc_arr
    
class Extracurr:
    def __init__(self, user_id, act_id):
        self.user_id = user_id
        self.act_id = act_id
        self.title = ''
        self.desc = ''

    def setData(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM extracurr WHERE act_id = ?', (self.act_id,))
        result = cursor.fetchone()

        self.title = result[2]
        self.desc = result[3]

        conn.close()

    def getData(self):
        return self.user_id, self.act_id, self.title, self.desc

class General_Info:
    def __init__(self, user_id):
        self.user_id = user_id
        self.lastname = ''
        self.firstname = ''
        self.phone = -1
        self.email = ''
        self.linkedin = ''
        self.edu = ''
        self.grad_date = ''
        self.major = ''
        self.GPA = 0.0

    def setData(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM general_info WHERE usr_id = ?', (self.user_id,))
        result = cursor.fetchone()
        self.lastname = result[1]
        self.firstname = result[2]
        self.phone = result[3]
        self.email = result[4]
        self.linkedin = result[5]
        self.edu = result[6]
        self.grad_date = result[7]
        self.major = result[8]
        self.GPA = result[9]

        conn.close()

    def getData(self):
        return self.user_id, self.lastname, self.firstname, self.phone, self.email, self.linkedin, self.edu, self.grad_date, self.major, self.GPA

class Technical_Skill:
    def __init__(self, user_id, skill_id):
        self.user_id = user_id
        self.skill_id = skill_id
        self.name = ''

    def setData(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM technical_skills WHERE skill_id = ?', (self.skill_id,))
        result = cursor.fetchone()
        self.name = result[2]

        conn.close()

    def getData():
        return user_id, skill_id, name

class Project:
    def __init__(self, user_id, proj_id):
        self.user_id = user_id
        self.proj_id = proj_id
        self.title = ''
        self.who_for = ''
        self.date = ''
        self.desc_arr = ''

    def setData(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM projects WHERE proj_id = ?', (self.proj_id,))
        result = cursor.fetchone()
        self.title = result[2]
        self.who_for = result[3]
        self.date = result[4]
        self.desc_arr = result[5]

        conn.close()

    def getData(self):
        return self.user_id, self.proj_id, self.title, self.who_for, self.date, self.desc_arr

class Award:
    def __init__(self, user_id, award_id):
        self.user_id = user_id
        self.award_id = award_id
        self.title = ''
        self.desc = ''

    def setData(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM awards WHERE awd_id = ?', (self.awd_id,))
        result = cursor.fetchone()

        self.title = result[2]
        self.desc = result[3]

        conn.close()

    def getData(self):
        return self.user_id, self.award_id, self.title, self.desc

class Course:
    def __init__(self, user_id, course_id):
        self.user_id = user_id
        self.course_id = course_id
        self.name = ''

    def setData(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM awards WHERE course_id = ?', (self.course_id,))
        result = cursor.fetchone()
        self.name = result[2]

        conn.close()

    def getData(self):
        return self.user_id, self.course_id, self.name

class Objective:
    def __init__(self, user_id):
        self.user_id = user_id
        self.obj_str = ''
        self.obj_id = -1

    def setData(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM awards WHERE usr_id = ?', (self.usr_id,))
        result = cursor.fetchone()

        self.obj_str = result[1]
        self.obj_id = result[2]

        conn.close()

    def getData(self):
        return self.user_id, self.obj_str, self.obj_id

class Volunteer_Work:
    def __init__(self, user_id, vol_id):
        self.user_id = user_id
        self.vol_id = vol_id
        self.company = ''
        self.role = ''
        self.start_date = ''
        self.end_date = ''

    def setData(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM awards WHERE usr_id = ?', (self.usr_id,))
        result = cursor.fetchone()

        self.company = result[2]
        self.role = result[3]
        self.start_date = result[4]
        self.end_date = result[5]

        conn.close()

    def getData(self):
        return self.user_id, self.vol_id, self.company, self.role, self.start_date, self.end_date

class Resume:
    def __init__(self):
        self.awards = []
        self.course_work = []
        self.experience = []
        self.extracurr = []
        self.general_info = []
        self.projects = []
        self.volunteer_work = []
        self.technical_skills = []
        self.objective = []

    def getUserInfo(self, id):
        # precondtion: id is an int
        # postcondition: gets user information for resume formatting

        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor() 

        cursor.execute('SELECT COUNT(*) FROM experience WHERE id = ?', (id,))
        result = cursor.fetchone()
        exp_id_exists = result[0] > 0

        cursor.execute('SELECT COUNT(*) FROM extracurr WHERE id = ?', (id,))
        result = cursor.fetchone()
        extracurr_id_exists = result[0] > 0

        cursor.execute('SELECT COUNT(*) FROM general_info WHERE id = ?', (id,))
        result = cursor.fetchone()
        general_id_exists = result[0] > 0

        cursor.execute('SELECT COUNT(*) FROM projects WHERE id = ?', (id,))
        result = cursor.fetchone()
        project_id_exists = result[0] > 0

        cursor.execute('SELECT COUNT(*) FROM technical_skills WHERE id = ?', (id,))
        result = cursor.fetchone()
        tech_id_exists = result[0] > 0

        if exp_id_exists and extracurr_id_exists and general_id_exists and project_id_exists and tech_id_exists:
            cursor.execute('SELECT COUNT(*) FROM awards WHERE id = ?', (id,))
            result = cursor.fetchone()
            awards_id = result[0] > 0
            cursor.execute('SELECT COUNT(*) FROM volunteer_work WHERE id = ?', (id,))
            result = cursor.fetchone()
            volunteer_work_id = result[0] > 0
            cursor.execute('SELECT COUNT(*) FROM objective WHERE id = ?', (id,))
            result = cursor.fetchone()
            objective_id = result[0] > 0
            cursor.execute('SELECT COUNT(*) FROM course_work WHERE id = ?', (id,))
            result = cursor.fetchone()
            course_work_id = result[0] > 0

            if awards_id and volunteer_work_id and objective_id and course_work_id:
                resume = Resume()
            resume = Resume()








    def addRecipe(id, recipes):

        #precondtion: id is an int, recipes is a list of Recipe objects
        #postcondition: adds recipe list to users(id) current list

        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(*) FROM experience WHERE id = ?', (id,))
        result = cursor.fetchone()
        exp_id_exists = result[0] > 0

        cursor.execute('SELECT COUNT(*) FROM extracurr WHERE id = ?', (id,))
        result = cursor.fetchone()
        extracurr_id_exists = result[0] > 0

        cursor.execute('SELECT COUNT(*) FROM general_info WHERE id = ?', (id,))
        result = cursor.fetchone()
        general_id_exists = result[0] > 0

        cursor.execute('SELECT COUNT(*) FROM projects WHERE id = ?', (id,))
        result = cursor.fetchone()
        project_id_exists = result[0] > 0

        cursor.execute('SELECT COUNT(*) FROM technical_skills WHERE id = ?', (id,))
        result = cursor.fetchone()
        tech_id_exists = result[0] > 0

        if exp_id_exists and extracurr_id_exists and general_id_exists and project_id_exists and tech_id_exists:

            cursor.execute("SELECT recipe_lists FROM recipes WHERE id = ?", (id,))
            result = cursor.fetchone()
            current_recipes_json = result[0] if result else '[]'
            current_recipes = json.loads(current_recipes_json)

            current_recipes.extend(recipes)

            updated_recipes_json = json.dumps(current_recipes, cls=RecipeEncoder)
            cursor.execute('UPDATE recipes SET recipe_lists = ? WHERE id = ?', (updated_recipes_json, id))
        
        else:
            recipes_json = json.dumps(recipes, cls=RecipeEncoder)
            cursor.execute('INSERT INTO recipes (id, recipe_lists) VALUES (?, ?)', (id, recipes_json))

        conn.commit()
        conn.close()

        return jsonify({'result': 'id does not exist'})
    
    def removeRecipe(id, name): 
        
        #precondition: id is an int, name is a string 
        #postcondition: removes the specified recipe if it exists

        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM recipes WHERE id = ?', (id,))
        result = cursor.fetchone()
        id_exists = result[0] > 0
        if id_exists:

            cursor.execute("SELECT recipe_lists FROM recipes WHERE id = ?", (id,))
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
            cursor.execute('UPDATE recipes SET recipe_lists = ? WHERE id = ?', (updated_recipes_json, id))

        conn.commit()
        conn.close()

    def getRecipes(id):

        #precondition: id must be an int (does not have to exist, there are check)
        #postcondition: returns json formatted list of all recipes associated with the id

        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM recipes WHERE id = ?', (id,))
        result = cursor.fetchone()
        id_exists = result[0] > 0
        if id_exists:
            cursor.execute("SELECT recipe_lists FROM recipes WHERE id = ?", (id,))
            result = cursor.fetchone()
            current_recipes_json = result[0] if result else '[]'
            return current_recipes_json
        return


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
    


# SAMPLE
# recipe = Recipe(
#     name='Gerber',
#     ingredients=['dough', 'tomato sauce', 'cheese'],
#     measurements = [(300, 'g'), (200, 'g'), (200, 'g')],
#     steps='Cook dough, add sauce and cheese'
# )
# recipes = [recipe]

# Recipe.addRecipe(0, recipes)
# Recipe.removeRecipe(0, 'Gerber')

experience = Experience(1)
experience.setData()
print(experience.getData())
conn = sqlite3.connect('server/usrDatabase/usrDB.db')
cursor = conn.cursor()
cursor.execute('SELECT job_id FROM experience WHERE usr_id=?', (1,))
result = cursor.fetchall()
job_ids = [results[0] for results in result]
print(job_ids)