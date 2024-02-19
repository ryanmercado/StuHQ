from flask import jsonify
import handleCreateAccount
import sqlite3

def login(username, password):
    #precondition: username and password are strings
    #postcondition: returns 'login successful' on success and 'login failed' on failed attempt
    hash_pswd =handleCreateAccount.hash_password(username, password)
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usr_info WHERE username = ? AND pswd_hash = ?', (username, hash_pswd))
    results = cursor.fetchone()
    cursor.close()
    conn.close()
    if results != None: #user exists
        return jsonify({
            'result': 'login successful',
            'usr_id': results[0]
            })
    else:
        return jsonify({'result': 'login failed'})

