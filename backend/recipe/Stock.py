import sqlite3
import json

class Stock:

    items = []

   

    def __init__(self):
        self.items = []

    
    def add_item(id, item):
        #precondition: id as int and item as string
        #postcondition: adds item to the stock list associated with id
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM curr_stock WHERE usr_id = ?', (id,))
        result = cursor.fetchone()
        id_exists = result[0] > 0

        if id_exists:
            cursor.execute("SELECT stock_list from curr_stock WHERE usr_id = ?", (id,))
            result = cursor.fetchone()
            current_stock_json = result[0] if result else '[]'
            item_exists = False
            current_stock = json.loads(current_stock_json)
            for existing_item in current_stock:
                if existing_item == item:
                    item_exists = True
            if not item_exists:
                current_stock.append(item)
                updated_stock_json = json.dumps(current_stock)
                cursor.execute('UPDATE curr_stock SET stock_list = ? WHERE usr_id = ?', (updated_stock_json, id))
            
        else:
            stock_list = [item]
            stock_list_json = json.dumps(stock_list)
            cursor.execute('INSERT INTO curr_stock (usr_id, stock_list) VALUES (?,?)', (id, stock_list_json))
            
        conn.commit()
        conn.close()


    def delete_item(id, del_item):
        #precondition: id as int and item as string
        #postcondition: deletes item from the stock list associated with id if it exists
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM curr_stock WHERE usr_id = ?', (id,))
        result = cursor.fetchone()
        id_exists = result[0] > 0

        if id_exists:
            cursor.execute("SELECT stock_list from curr_stock WHERE usr_id = ?", (id,))
            result = cursor.fetchone()
            current_stock_json = result[0] if result else '[]'

            current_stock = json.loads(current_stock_json)
            new_stock = []

            for item in current_stock:
                if item == del_item:
                    continue
                else: 
                    new_stock.append(item)

            updated_stock_json = json.dumps(new_stock)
            cursor.execute('UPDATE curr_stock SET stock_list = ? WHERE usr_id = ?', (updated_stock_json, id))
            
        conn.commit()
        conn.close()

    def get_items(id):
        #precondition: id as int and item as string
        #postcondition: returns all items in the stock list associated with id
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM curr_stock WHERE usr_id = ?', (id,))
        result = cursor.fetchone()
        id_exists = result[0] > 0

        if id_exists:
            cursor.execute("SELECT stock_list from curr_stock WHERE usr_id = ?", (id,))
            result = cursor.fetchone()
            current_stock_json = result[0] if result else '[]'
            return current_stock_json
        return


# Stock.add_item(1, 'strawbs')
# Stock.delete_item(0, 'strawbs')
# print(Stock.get_items(1))