from flask import jsonify
import handleCreateAccount
import sqlite3

def login(username, password):
    hash_pswd =handleCreateAccount.hash_password(username, password)
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usr_info WHERE username = ? AND pswd_hash = ?', (username, hash_pswd))
    results = cursor.fetchone()
    if results[0] > 0: #user exists
        return jsonify({'result': 'log in successful'})
    else:
        return jsonify({'result': 'login failed'})

