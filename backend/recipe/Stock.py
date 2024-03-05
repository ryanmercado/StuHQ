import sqlite3
import json
from flask import jsonify

class Stock:

    items = []

   

    def __init__(self):
        self.items = []

    
    def add_item(id, item):
        #precondition: id as int and item as string
        #postcondition: adds item to the stock list associated with id
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM usr_info WHERE usr_id = ?', (id,))
        result = cursor.fetchone()

        if result[0] > 0:
            cursor.execute("SELECT stock_list from curr_stock WHERE usr_id = ?", (id,))
            result = cursor.fetchone()
            if result != None:
                current_stock = result[0] if result else '[]'
                current_stock = current_stock.split(', ')
                item_exists = False
                for existing_item in current_stock:
                    if existing_item == item:
                        item_exists = True
                if not item_exists:
                    current_stock.append(item)
                    items_string = ', '.join(current_stock)
                    cursor.execute('UPDATE curr_stock SET stock_list = ? WHERE usr_id = ?', (items_string, id))
            else:
                cursor.execute('INSERT INTO curr_stock (usr_id, stock_list) VALUES (?, ?)', (id, item))
            
        conn.commit()
        cursor.close()
        conn.close()


    def delete_item(id, del_item):
        #precondition: id as int and item as string
        #postcondition: deletes item from the stock list associated with id if it exists
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM usr_info WHERE usr_id = ?', (id,))
        result = cursor.fetchone()

        if result[0] > 0:
            cursor.execute("SELECT stock_list from curr_stock WHERE usr_id = ?", (id,))
            result = cursor.fetchone()
            current_stock = result[0] if result else '[]'
            current_stock = current_stock.split(', ')
            new_stock = []
            for item in current_stock:
                if item == del_item:
                    continue
                else: 
                    new_stock.append(item)
            items_string = ', '.join(new_stock)
            if items_string:
                cursor.execute('UPDATE curr_stock SET stock_list = ? WHERE usr_id = ?', (items_string, id))
            else:
                cursor.execute('DELETE FROM curr_stock WHERE usr_id = ?', (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def get_items(id):
        #precondition: id as int and item as string
        #postcondition: returns all items in the stock list associated with id
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM curr_stock WHERE usr_id = ?', (id,))
        result = cursor.fetchone()

        if result[0] > 0: # user exists
            cursor.execute("SELECT stock_list FROM curr_stock WHERE usr_id = ?", (id,))
            result = cursor.fetchone()
            current_stock = result[0] if result else '[]'
            cursor.close()
            conn.close()
            return json.dumps(current_stock)
        cursor.close()
        conn.close()
        return jsonify({'result': 'usr did not exist'})