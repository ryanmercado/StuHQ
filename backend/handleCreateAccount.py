from flask import jsonify
import sqlite3
import hashlib
from datetime import datetime

def get_id():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(usr_id) FROM usr_info')
    max_id = cursor.fetchone()[0]
    if max_id == None:
        return 0

    # Iterate over the range of usr_ids from 1 to the maximum
    for usr_id in range(0, max_id + 1):
        # Check if the usr_id exists in the usr_info table
        cursor.execute('SELECT COUNT(*) FROM usr_info WHERE usr_id = ?', (usr_id,))
        count = cursor.fetchone()[0]
        if count == 0:
            # Found the first missing usr_id
            return usr_id

    # If all usr_ids from 1 to the maximum are present, return the next available id
    return max_id + 1

def hash_password(username, password):
    to_hash = username + password
    to_hash_bytes = to_hash.encode('utf-8')
    hasher = hashlib.sha256()
    hasher.update(to_hash_bytes)
    hashed_password = hasher.hexdigest()
    return hashed_password


def sign_up(username, email, password, confirm_password):
    #precondition: username, email, password, confirm_password are strings
    #postcondition: returns 3 different error messages for failed cases
    #           'username already exists' 
    #           'passwords do not match'
    #           'a user has already signed up with this email'
    # returns 'account created successfully' on successful creation

    if password != confirm_password: #if passwords do not match
            print('found')
            return jsonify({'result': 'passwords do not match'})
    
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usr_info WHERE username = ?", (username,)) 
    results = cursor.fetchone()
    if results != None:
        if results[0] > 0: #if username exists
            cursor.close()
            conn.close()
            return jsonify({'result': 'username already exists'})
    
        cursor.execute('SELECT * FROM usr_info WHERE usr_email = ?', (email,)) #if email is associated with a user
        results = cursor.fetchone()
        if results != None:
            cursor.close()
            conn.close()
            return jsonify({'result': 'a user has already signed up with this email'})
    
        next_id = get_id()
        pswd_hash = hash_password(username, password)
        created_epoch = datetime.now().timestamp()
        cursor.execute("INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (?,?, ?, ?, ?)", (next_id, username,
        pswd_hash, email, created_epoch ))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'result': 'account created successfully'})
    else:
        next_id = get_id()
        pswd_hash = hash_password(username, password)
        created_epoch = datetime.now().timestamp()
        cursor.execute("INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (?,?, ?, ?, ?)", (next_id, username,
        pswd_hash, email, created_epoch ))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'result': 'account created successfully'})
    
# if __name__ == '__main__':
#     sign_up('grayghost34', 'grayson.drinkard@gmail.com', 'gerber', 'gerber')
    
    
    