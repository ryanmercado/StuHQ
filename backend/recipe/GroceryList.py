import sqlite3
import json
import Stock

class GroceryList:
    items = []

    def __init__(self):
        self.items = []


    def add_item(id, item):
        #precondition: id as int and item as string
        #postcondition: adds item to the grocery list associated with id
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM grocery_list WHERE usr_id = ?', (id,))
        results = cursor.fetchone()
        if results[0] > 0: #if user exists
            cursor.execute('SELECT grocery_list FROM grocery_list WHERE usr_id = ?', (id,))
            results = cursor.fetchone()
            current_grocery_list_json = results[0] if results else '[]'
            current_grocery_list = json.loads(current_grocery_list_json)
            item_exists = False

            for existing_item in current_grocery_list:
                if existing_item == item:
                    item_exists = True
            
            if not item_exists:
                current_grocery_list.append(item)
                final_grocery_list = json.dumps(current_grocery_list)
                cursor.execute('UPDATE grocery_list SET grocery_list = ? WHERE usr_id = ?', (final_grocery_list, id))

        else:
            grocery_list = [item]
            final_grocery_list = json.dumps(grocery_list)
            cursor.execute("INSERT INTO grocery_list (usr_id, grocery_list) VALUES (?,?)", (id, final_grocery_list))

        conn.commit()
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
            current_grocery_list_json = results[0] if results else '[]'
            current_grocery_list = json.loads(current_grocery_list_json)
            shaved_grocery_list = []
            for existing_item in current_grocery_list:
                if existing_item == item:
                    continue
                else:
                    shaved_grocery_list.append(existing_item)
            final_grocery_list = json.dumps(shaved_grocery_list)
            cursor.execute('UPDATE grocery_list SET grocery_list = ? WHERE usr_id = ?', (final_grocery_list, id))

        conn.commit()
        conn.close()

    def get_items(id):
        #precondition: id as int
        #postcondition: returns all items in the grocery list associated with id
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM grocery_list WHERE usr_id = ?', (id,))
        results = cursor.fetchone()

        if results[0] > 0: #if user exists
            cursor.execute('SELECT grocery_list FROM grocery_list WHERE usr_id = ?', (id,))
            results = cursor.fetchone()
            current_grocery_list_json = results[0] if results else '[]'
            return current_grocery_list_json
        
        return


    def purchased_item(id, item):
        #precondition: id as int and item as string
        #postcondition: removes item from grocery list, adds item to stock
        GroceryList.delete_item(id, item)
        Stock.add_item(id, item)


# GroceryList.delete_item(1, 'grapes')
# GroceryList.add_item(1, 'strawbs')
# print(GroceryList.get_items(0))