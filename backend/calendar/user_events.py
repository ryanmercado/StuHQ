import sqlite3
from check_ids import usr_id_exists, event_id_exists, UserNotFoundException, EventNotFoundException
from datetime import datetime

def create_event(usr_id, event_id, created_epoch, event_desc, event_type, 
                 event_title, start_epoch, end_epoch, on_to_do_list, extra_data, 
                 is_submitted, want_notification):
    if(usr_id_exists(usr_id)):
        con = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = con.cursor()
        cursor.execute('''
            INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type,
                                event_title, start_epoch, end_epoch, on_to_do_list, extra_data, 
                                is_submitted, want_notification)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (usr_id, event_id, created_epoch, event_desc, event_type,
            event_title, start_epoch, end_epoch, on_to_do_list, extra_data,
            is_submitted, want_notification))
        
        con.commit()
        con.close()
    else:
        raise UserNotFoundException

def read_event(event_id):
    if event_id_exists(event_id):
        con = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM calendar WHERE event_id = ?', (event_id,))
        event = cursor.fetchone()
        con.close()
        return event
    else:
        raise EventNotFoundException

def read_usr_events(usr_id):
    if usr_id_exists(usr_id):
        con = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM calendar WHERE usr_id = ?', (usr_id,))
        events = cursor.fetchall()
        con.close()
        return events
    else:
        raise UserNotFoundException


def update_event(event_id, event_title, event_desc, event_type, start_epoch, end_epoch, on_to_do_list, is_submitted, want_notification):
    if event_id_exists(event_id):
        con = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = con.cursor()
        cursor.execute('''UPDATE calendar 
                          SET event_title = ?, event_desc = ?, event_type = ?, start_epoch = ?, 
                          end_epoch = ?, on_to_do_list = ?, is_submitted = ?, want_notification = ?
                          WHERE event_id = ?''', (event_title, event_desc, event_type, start_epoch, end_epoch, on_to_do_list, is_submitted, want_notification, event_id))
        con.commit()
        con.close()
    else:
        raise EventNotFoundException

def delete_event(event_id):
    if event_id_exists(event_id):
        con = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = con.cursor()
        cursor.execute('DELETE FROM calendar WHERE event_id = ?', (event_id,))
        con.commit()
        con.close()
    else:
        raise EventNotFoundException


