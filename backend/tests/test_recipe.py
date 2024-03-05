import sqlite3
import pytest
from backend.recipe import GroceryList, Recipe, Stock
from flask import Flask
import json

#Cases:
#   Recipe:
#       - add recipe(user exists, empty list) 
#           Test: test_add_recipe
#
#       - add recipe (user exist, populated list) 
#           Test: test_add_recipe2
#
#       - add recipe (user does not exist) 
#           Test: test_add_recipe3
#
#       - remove recipe (user exists, recipe exists)
#           Test: test_remove_recipe
#
#       - remove recipe (user exists, recipe does not exist)
#           Test: test_remove_recipe2
#
#       - remove recipe (user does not exist)
#           Test: test_remove_recipe3
#
#       - get recipes (user exists, one item in list)
#           Test: test_get_recipes
#
#       - get recipes (user exists, multiple items in list)
#           Test: test_get_recipes2
#
#       - get recipes (user does not exist)
#           Test: test_get_recipes3
#
#   GroceryList:
#       -add item (user exists, empty list)
#           Test: test_add_grocery_item2
#
#       -add item (user exists, populated list)
#           Test: test_add_grocery_item
#
#       -add item (user does not exist)
#           Test: test_add_grocery_item3
#
#       -delete item (user does not exist, nothing happens)
#           Test: test_grocery_item
#
#       -delete item (existing item)
#           Test: test_remove_grocery_item3
#
#       -delete item (empty list)
#           Test: test_remove_grocery_item4
#
#       -delete item (populated list, item missing)
#           Test: test_remove_grocery_item2
#
#       -get items (user does not exist)
#           Test:
#
#       -get items (user exists, populated list)
#           Test:
#
#       -get items (user exists, empty list)
#           Test:
#   
#   Stock:
#
#
#
#


# Define a mock Flask app for testing
def create_test_app():
    app = Flask(__name__)
    # Add any necessary configuration or routes for your mock app
    return app

# Use this function to create a mock Flask app
app = create_test_app()

@pytest.fixture(scope='module')
def app_client():
    with app.app_context():
        yield app.test_client()


@pytest.fixture
def populate_grocery_list_fixture():
    add_grocery_list()
    
@pytest.fixture
def populate_recipes_list_fixture():
    add_recipes_list()

@pytest.fixture
def populate_stock_list_fixture():
    add_stock_list()
        
@pytest.fixture
def clear_db_fixture():
    clear_db()
    yield

@pytest.fixture
def user_exists_fixture():
    add_user()
    yield

def add_user():
    clear_db()
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (?, ?, ?, ?, ?)', (0, 'gray', 'hash', 'g@email.com', 1))
    conn.commit()
    cursor.close()
    conn.close()

    
def clear_db():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usr_info')
    cursor.execute('DELETE FROM grocery_list')
    cursor.execute('DELETE FROM recipes')
    cursor.execute('DELETE FROM curr_stock')
    conn.commit()
    cursor.close()
    conn.close()

def add_recipes_list():
    recipe = Recipe.Recipe(
        name='Pizza',
        ingredients=['dough', 'tomato sauce', 'cheese'],
        measurements = [(300, 'g'), (200, 'g'), (200, 'g')],
        steps='Cook dough, add sauce and cheese'
    )
    recipes = [recipe]
    Recipe.Recipe.addRecipe(0, recipes)

def add_stock_list():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO curr_stock (usr_id, stock_list) VALUES (?,?)', (0, "grapes, beans"))
    conn.commit()
    cursor.close()
    conn.close()

def add_grocery_list():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO grocery_list (usr_id, grocery_list) VALUES (?,?)', (0, "grapes, beans"))
    conn.commit()
    cursor.close()
    conn.close()

# START OF STOCK TESTS
def test_add_stock_item(user_exists_fixture, populate_stock_list_fixture): #add item (user exists, populated list)
    Stock.Stock.add_item(0, 'pretzels')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM curr_stock WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res[0] == 0)
    assert (res[1] == 'grapes, beans, pretzels')

def test_add_stock_item2(user_exists_fixture): #add item (user exists, empty list)
    Stock.Stock.add_item(0, 'pretzels')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM curr_stock WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res[0] == 0)
    assert (res[1] == 'pretzels')

def test_add_stock_item3(clear_db_fixture): #add item (user does not exist)
    Stock.Stock.add_item(0, 'pretzels')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM curr_stock WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res == None)


def test_remove_stock_item(clear_db_fixture):  # delete item (user does not exist)
    Stock.Stock.delete_item(0, 'pretzels')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM curr_stock WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res == None)

def test_remove_stock_item2(user_exists_fixture, populate_stock_list_fixture):  # delete item (populated list, item missing)
    Stock.Stock.delete_item(0, 'pretzels')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM curr_stock WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res[0] == 0)
    assert (res[1] == 'grapes, beans')

def test_remove_stock_item3(user_exists_fixture, populate_stock_list_fixture): #delete item (existing item)
    Stock.Stock.delete_item(0, 'grapes')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM curr_stock WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res[0] == 0)
    assert (res[1] == 'beans')

def test_remove_stock_item4(user_exists_fixture, populate_stock_list_fixture): # delete item (empty list)
    Stock.Stock.delete_item(0, 'grapes')
    Stock.Stock.delete_item(0, 'beans')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM curr_stock WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res == None)
    GroceryList.GroceryList.delete_item(0, 'grapes')
    cursor.execute('SELECT * FROM curr_stock WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res == None)

def test_get_stock_item(clear_db_fixture, app_client): # get items (user does not exist)
    list = Stock.Stock.get_items(0)
    res = list.get_json()
    assert (res['result'] == 'usr did not exist' )


def test_get_stock_item2(user_exists_fixture, populate_stock_list_fixture): # get items (user exists, populated list)
    list = Stock.Stock.get_items(0)
    assert (list == '"grapes, beans"')

def test_get_stock_item3(user_exists_fixture, populate_stock_list_fixture): # get items (user exists, empty list)
    Stock.Stock.delete_item(0, 'grapes')
    Stock.Stock.delete_item(0, 'beans')
    response = Stock.Stock.get_items(0)
    data = response.get_json()  # Convert the response to a dictionary
    assert data['result'] == 'usr did not exist'



    
#START OF GROCERY TESTS
    
def test_add_grocery_item(user_exists_fixture, populate_grocery_list_fixture): #add item (user exists, populated list)
    GroceryList.GroceryList.add_item(0, 'pretzels')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grocery_list WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res[0] == 0)
    assert (res[1] == 'grapes, beans, pretzels')

def test_add_grocery_item2(user_exists_fixture): #add item (user exists, empty list)
    GroceryList.GroceryList.add_item(0, 'pretzels')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grocery_list WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res[0] == 0)
    assert (res[1] == 'pretzels')

def test_add_grocery_item3(clear_db_fixture): #add item (user does not exist)
    GroceryList.GroceryList.add_item(0, 'pretzels')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grocery_list WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res == None)


def test_remove_grocery_item(clear_db_fixture):  # delete item (user does not exist)
    GroceryList.GroceryList.delete_item(0, 'pretzels')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grocery_list WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res == None)

def test_remove_grocery_item2(user_exists_fixture, populate_grocery_list_fixture):  # delete item (populated list, item missing)
    GroceryList.GroceryList.delete_item(0, 'pretzels')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grocery_list WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res[0] == 0)
    assert (res[1] == 'grapes, beans')

def test_remove_grocery_item3(user_exists_fixture, populate_grocery_list_fixture): #delete item (existing item)
    GroceryList.GroceryList.delete_item(0, 'grapes')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grocery_list WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res[0] == 0)
    assert (res[1] == 'beans')

def test_remove_grocery_item4(user_exists_fixture, populate_grocery_list_fixture): # delete item (empty list)
    GroceryList.GroceryList.delete_item(0, 'grapes')
    GroceryList.GroceryList.delete_item(0, 'beans')
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grocery_list WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res == None)
    GroceryList.GroceryList.delete_item(0, 'grapes')
    cursor.execute('SELECT * FROM grocery_list WHERE usr_id = ?', (0, ))
    res = cursor.fetchone()
    assert (res == None)

def test_get_grocery_item(clear_db_fixture, app_client): # get items (user does not exist)
    list = GroceryList.GroceryList.get_items(0)
    res = list.get_json()
    assert (res['result'] == 'id did not exist' )


def test_get_grocery_item2(user_exists_fixture, populate_grocery_list_fixture): # get items (user exists, populated list)
    list = GroceryList.GroceryList.get_items(0)
    assert (list == '"grapes, beans"')

def test_get_grocery_item3(): # get items (user exists, empty list)
    GroceryList.GroceryList.delete_item(0, 'grapes')
    GroceryList.GroceryList.delete_item(0, 'beans')
    list = GroceryList.GroceryList.get_items(0)
    res = list.get_json()
    assert (res['result'] == 'id did not exist')
    



#START OF RECIPE TESTS


def test_add_recipe(user_exists_fixture): #add recipe (user exists, empty list)
    recipe = Recipe.Recipe(
        name='Grayson',
        ingredients=['dough', 'tomato sauce', 'cheese'],
        measurements = [(300, 'g'), (200, 'g'), (200, 'g')],
        steps='Cook dough, add sauce and cheese'
    )
    recipes = [recipe]
    Recipe.Recipe.addRecipe(0, recipes)
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recipes WHERE usr_id = ?', (0,))
    result = cursor.fetchone()
    assert (result[0] == 0)
    assert (result[1] == '[{"name": "Grayson", "ingredients": ["dough", "tomato sauce", "cheese"], "measurements": [[300, "g"], [200, "g"], [200, "g"]], "steps": "Cook dough, add sauce and cheese"}]')
    conn.commit()
    cursor.close()
    conn.close()

def test_add_recipe2(user_exists_fixture, populate_recipes_list_fixture): #add recipe (user exists, populated list)
    recipe = Recipe.Recipe(
        name='Pasta',
        ingredients=['dough', 'tomato sauce', 'cheese'],
        measurements = [(300, 'g'), (200, 'g'), (200, 'g')],
        steps='Cook dough, add sauce and cheese'
    )
    recipes = [recipe]
    Recipe.Recipe.addRecipe(0, recipes)
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recipes WHERE usr_id = ?', (0,))
    result = cursor.fetchone()
    assert (result[0] == 0)
    assert (result[1] == '[{"name": "Pizza", "ingredients": ["dough", "tomato sauce", "cheese"], "measurements": [[300, "g"], [200, "g"], [200, "g"]], "steps": "Cook dough, add sauce and cheese"}, {"name": "Pasta", "ingredients": ["dough", "tomato sauce", "cheese"], "measurements": [[300, "g"], [200, "g"], [200, "g"]], "steps": "Cook dough, add sauce and cheese"}]')
    conn.commit()
    cursor.close()
    conn.close()

def test_add_recipe3(clear_db_fixture):     #add recipe (user does not exist) (nothing should change in db if user does not exist in usr_info table)
    recipe = Recipe.Recipe(
        name='Pasta',
        ingredients=['dough', 'tomato sauce', 'cheese'],
        measurements = [(300, 'g'), (200, 'g'), (200, 'g')],
        steps='Cook dough, add sauce and cheese'
    )
    recipes = [recipe]
    Recipe.Recipe.addRecipe(0, recipes)
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recipes WHERE usr_id = ?', (0, ))
    res = cursor.fetchone() 
    assert (res == None)

def test_remove_recipe(user_exists_fixture, populate_recipes_list_fixture): #remove recipe (user exists, recipe exists)
    name = 'Pizza'
    Recipe.Recipe.removeRecipe(0, name)
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recipes WHERE usr_id = ?', (0,))
    res = cursor.fetchone()
    assert (res[0] == 0)
    assert (res[1] == '[]')

def test_remove_recipe2(user_exists_fixture, populate_recipes_list_fixture): #remove recipe (user exists, recipe exists)
    name = 'Pasta'
    Recipe.Recipe.removeRecipe(0, name)
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recipes WHERE usr_id = ?', (0,))
    res = cursor.fetchone()
    assert (res[0] == 0)
    assert (res[1] == '[{"name": "Pizza", "ingredients": ["dough", "tomato sauce", "cheese"], "measurements": [[300, "g"], [200, "g"], [200, "g"]], "steps": "Cook dough, add sauce and cheese"}]')

def test_remove_recipe3(clear_db_fixture): #remove recipe (user does not exist)
    name = 'Pasta'
    Recipe.Recipe.removeRecipe(0, name)
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recipes WHERE usr_id = ?', (0,))
    res = cursor.fetchone()
    assert (res == None)

def test_get_recipes(user_exists_fixture, populate_recipes_list_fixture): #get recipes (user exists, one item in list)
    recipes = Recipe.Recipe.getRecipes(0)
    assert (recipes == '[{"name": "Pizza", "ingredients": ["dough", "tomato sauce", "cheese"], "measurements": [[300, "g"], [200, "g"], [200, "g"]], "steps": "Cook dough, add sauce and cheese"}]')

def test_get_recipes2(user_exists_fixture, populate_recipes_list_fixture): #get recipes (user exists, multiple items in list)
    recipe = Recipe.Recipe(
        name='Pasta',
        ingredients=['dough', 'tomato sauce', 'cheese'],
        measurements = [(300, 'g'), (200, 'g'), (200, 'g')],
        steps='Cook dough, add sauce and cheese'
    )
    recipes = [recipe]
    Recipe.Recipe.addRecipe(0, recipes)

    recipes = Recipe.Recipe.getRecipes(0)
    assert (recipes == '[{"name": "Pizza", "ingredients": ["dough", "tomato sauce", "cheese"], "measurements": [[300, "g"], [200, "g"], [200, "g"]], "steps": "Cook dough, add sauce and cheese"}, {"name": "Pasta", "ingredients": ["dough", "tomato sauce", "cheese"], "measurements": [[300, "g"], [200, "g"], [200, "g"]], "steps": "Cook dough, add sauce and cheese"}]')

def test_get_recipes3(clear_db_fixture, app_client): #get recipes (user does not exist)
    res = Recipe.Recipe.getRecipes(0)
    data = res.json
    assert (data['result'] == 'id did not exist')    



    
