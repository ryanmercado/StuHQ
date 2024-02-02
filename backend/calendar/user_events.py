import sqlite3
from datetime import datetime

def create_event(usr_id, event_id, created_epoch, event_desc, event_type, 
                 event_title, start_epoch, end_epoch, is_important, extra_data, 
                 is_submitted, want_notification):
    con = sqlite3.connect('/home/cdew/StuHQ/server/usrDatabase/usrDB.db')
    cursor = con.cursor()
    cursor.execute('''
        INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type,
                              event_title, start_epoch, end_epoch, is_important, extra_data, 
                              is_submitted, want_notification)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (usr_id, event_id, created_epoch, event_desc, event_type,
          event_title, start_epoch, end_epoch, is_important, extra_data,
          is_submitted, want_notification))
    
    con.commit()
    con.close()

def read_event(event_id):
    con = sqlite3.connect('/home/cdew/StuHQ/server/usrDatabase/usrDB.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM calendar WHERE event_id = ?', (event_id,))
    event = cursor.fetchone()
    con.close()
    return event

def update_event(event_id, new_event_title):
    con = sqlite3.connect('/home/cdew/StuHQ/server/usrDatabase/usrDB.db')
    cursor = con.cursor()
    cursor.execute('UPDATE calendar SET event_title = ? WHERE event_id = ?', (new_event_title, event_id))
    con.commit()
    con.close()

def delete_event(event_id):
    con = sqlite3.connect('/home/cdew/StuHQ/server/usrDatabase/usrDB.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM calendar WHERE event_id = ?', (event_id,))
    con.commit()
    con.close()



