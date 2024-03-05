import sqlite3
from flask import jsonify
from datetime import datetime


def create_event(usr_id, event_desc, event_type, 
                 event_title, start_epoch = None, end_epoch = None,  on_to_do_list = 0, extra_data = None, 
                 is_submitted = None, want_notification = None):
    
    '''
        precondition: 
            usr_id exists in db as INT, not NULL
            event_desc is TEXT, not NULL
            event_type is VARCHAR(50), not NULL
            event_title is VARCHAR(50), not NULL
            start_epoch is INT, NULLABLE
            end_epoch is INT, NULLABLE
            on_to_do_list is BOOLEAN, not NULL
            extra_data is VARCHAR(250), NULLABLE
            is_submitted is BOOLEAN, NULLABLE
            want_notification is BOOLEAN, NULLABLE

        postcondition:
            inputs given values into DB, assiging event to usr_id
            returns error if usr_id not found
            returns success message if successful 

    '''

    if(usr_id_exists(usr_id)):
        created_epoch = datetime.now().timestamp()
        next_id = get_event_id()
        con = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = con.cursor()
        cursor.execute('''
            INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type,
                                event_title, start_epoch, end_epoch, on_to_do_list, extra_data, 
                                is_submitted, want_notification)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (usr_id, next_id, created_epoch, event_desc, event_type,
            event_title, start_epoch, end_epoch, on_to_do_list, extra_data,
            is_submitted, want_notification))
        
        con.commit()
        con.close()
        return jsonify({'result': 'event created'})
    else:
        return jsonify({'result': 'id not found'}) 


def get_event(event_id):

    '''
        precondition:
            event_id is in DB as INT

        postcondition:
            returns event information
            returns error if event_id does not exist
    '''


    if event_id_exists(event_id):
        con = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM calendar WHERE event_id = ?', (event_id,))
        result = cursor.fetchone()
        event = result
        con.close()
        return jsonify({'result': event}) 
    else:
        return jsonify({'result': 'event not found'}) 

def get_usr_events(usr_id):

    '''
        precondition:
            usr_id is in DB as INT

        postcondition:
            returns all event information
            returns error if usr_id does not exist
    '''

    if usr_id_exists(usr_id):
        con = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM calendar WHERE usr_id = ?', (usr_id,))
        result = cursor.fetchall()
        events = result
        con.close()
        return jsonify({'result': events}) 
    else:
        return jsonify({'result': 'usr_id not found'})


def update_event(event_id, event_title, event_desc, event_type, start_epoch, end_epoch, on_to_do_list, extra_data, is_submitted, want_notification):

    '''
        precondition:
            event_id exists in db as INT, not NULL
            event_title is VARCHAR(50), not NULL
            event_desc is TEXT, not NULL
            event_type is VARCHAR(50), not NULL
            start_epoch is INT, NULLABLE
            end_epoch is INT, NULLABLE
            on_to_do_list is BOOLEAN, not NULL
            extra_data is VARCHAR(250), NULLABLE
            is_submitted is BOOLEAN, NULLABLE
            want_notification is BOOLEAN, NULLABLE

        postcondition:
            updates event information in DB
            returns success message if succesful
            returns error if event_id does not exist
    '''

    if event_id_exists(event_id):
        con = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = con.cursor()
        cursor.execute('''UPDATE calendar 
                          SET event_title = ?, event_desc = ?, event_type = ?, start_epoch = ?, 
                          end_epoch = ?, on_to_do_list = ?, is_submitted = ?, want_notification = ?, extra_data = ?
                          WHERE event_id = ?''', (event_title, event_desc, event_type, start_epoch, end_epoch, on_to_do_list, is_submitted, want_notification, extra_data, event_id))
        con.commit()
        con.close()
        return jsonify({'result': 'event updated'}) 
    else:
        return jsonify({'result': 'event_id not found'}) 

def delete_event(event_id):

    '''
        precondition:
            event_id exists in db as INT, not NULL

        postcondition:
            deletes event information from DB
            returns success message if succesful
            returns error if event_id does not exist
    '''

    if event_id_exists(event_id):
        con = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = con.cursor()
        cursor.execute('DELETE FROM calendar WHERE event_id = ?', (event_id,))
        con.commit()
        con.close()
        return jsonify({'result': 'event_id deleted'}) 
    else:
        return jsonify({'result': 'event_id not found'}) 
    
def get_event_id():

    '''
        returns a new unique event_id 
    '''

    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(event_id) FROM calendar')
    max_id = cursor.fetchone()[0]

    if max_id is not None:
        # Iterate over the range of usr_ids from 1 to the maximum
        for event_id in range(0, max_id + 1):
            # Check if the usr_id exists in the usr_info table
            cursor.execute('SELECT COUNT(*) FROM calendar WHERE event_id = ?', (event_id,))
            count = cursor.fetchone()[0]
            if count == 0:
                # Found the first missing usr_id
                return event_id
    else:
        return 0

    # If all usr_ids from 1 to the maximum are present, return the next available id
    return max_id + 1



def usr_id_exists(usr_id):

    '''
        precondition: 
            usr_id is an INT

        postcondition:
            returns a boolean
                TRUE if usr_id is in DB
                FALS if usr_id is not in DB
    '''

    con = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = con.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM usr_info WHERE usr_id = ?', (usr_id,))
    count = cursor.fetchone()[0]
    
    con.close()

    return count > 0

def event_id_exists(event_id):

    '''
        precondition: 
            event_id is an INT

        postcondition:
            returns a boolean
                TRUE if event_id is in DB
                FALS if event_id is not in DB
    '''

    con = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = con.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM calendar WHERE event_id = ?', (event_id,))
    count = cursor.fetchone()[0]
    
    con.close()

    return count > 0

def toggleToDo(event_id, on_to_do_list):
    if event_id_exists(event_id):
        con = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = con.cursor()
        cursor.execute('''
                       UPDATE calendar 
                       SET on_to_do_list = ?
                       WHERE event_id = ?
                       ''', (on_to_do_list,event_id,))
        con.commit()
        con.close()
        return jsonify({'result': 'toggle successful'}) 
    else:
        return jsonify({'result': 'event_id not found'}) 
