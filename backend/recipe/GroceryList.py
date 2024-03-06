import sqlite3
import json
from recipe import Stock
from flask import jsonify

class GroceryList:
    items = []

    def __init__(self):
        self.items = []


    def add_item(id, item):
        #precondition: id as int and item as string
        #postcondition: adds item to the grocery list associated with id
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM usr_info WHERE usr_id = ?', (id,))
        results = cursor.fetchone()
        if results[0] > 0: #if user exists
            cursor.execute('SELECT grocery_list FROM grocery_list WHERE usr_id = ?', (id,))
            results = cursor.fetchone()
            if results != None:
                current_grocery_list_json = results[0]
                items_list = current_grocery_list_json.split(', ')
                item_exists = False

                for existing_item in items_list:
                    if existing_item == item:
                        item_exists = True
            
                if not item_exists:
                    items_list.append(item)
                    items_string = ', '.join(items_list)
                    # final_grocery_list = json.dumps(current_grocery_list)
                    cursor.execute('UPDATE grocery_list SET grocery_list = ? WHERE usr_id = ?', (items_string, id))
            else: 
                cursor.execute('INSERT INTO grocery_list (usr_id, grocery_list) VALUES (?,?)', (id, item))
            

        conn.commit()
        cursor.close()
        conn.close()

    def delete_item(id, item):
        #precondition: id as int and item as string
        #postcondition: deletes item from the grocery list associated with id
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM grocery_list WHERE usr_id = ?', (id,))
        results = cursor.fetchone()
        if results[0] > 0: #if user exists
            cursor.execute('SELECT grocery_list FROM grocery_list WHERE usr_id = ?', (id,))
            results = cursor.fetchone()
            current_grocery_list = results[0] if results else '[]'
            shaved_grocery_list = []
            items_list = current_grocery_list.split(', ')
            for existing_item in items_list:
                if existing_item == item:
                    continue
                else:
                    shaved_grocery_list.append(existing_item)
            final_list = ', '.join(shaved_grocery_list)
            if final_list: 
                cursor.execute('UPDATE grocery_list SET grocery_list = ? WHERE usr_id = ?', (final_list, id))
            else:
                cursor.execute('DELETE FROM grocery_list WHERE usr_id = ?', (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def get_items(id):
        #precondition: id as int
        #postcondition: returns all items in the grocery list associated with id
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM grocery_list WHERE usr_id = ?', (id,))
        results = cursor.fetchone()

        if results[0] > 0: # if user exists
            cursor.execute('SELECT grocery_list FROM grocery_list WHERE usr_id = ?', (id,))
            results = cursor.fetchone()
            current_grocery_list = results[0] if results else '[]'
            cursor.close()
            conn.close()
            return json.dumps(current_grocery_list)
        cursor.close()
        conn.close()
        return jsonify({'result': 'id did not exist'})


    def purchased_item(id, item):
        #precondition: id as int and item as string
        #postcondition: removes item from grocery list, adds item to stock
        GroceryList.delete_item(id, item)
        Stock.Stock.add_item(id, item)