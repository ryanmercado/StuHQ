import sqlite3
from backend.calendar_module import user_events

# Clears usr_info and calendar tables
def clearDB():
    con = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM usr_info')
    cursor.execute('DELETE FROM calendar')
    con.commit()
    con.close()

def test_get_event_id():
    clearDB()
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    x0 = user_events.get_event_id()
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (1, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (1, 0, 1234567890, "description", "assignment", "HW1", 1);')
    con.commit()
    con.close()
    x1 = user_events.get_event_id()

    assert x0 == 0
    assert x1 == 1

    clearDB()

def test_usr_id_exists():
    clearDB()
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    # Add test data to the database
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    con.commit()
    con.close()

    assert user_events.usr_id_exists(0) is True
    assert user_events.usr_id_exists(1) is False

    clearDB()

def test_event_id_exists():
    clearDB()
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    # Add test data to the database
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (1, 0, 1234567890, "description", "assignment", "HW1", 1);')
    con.commit()
    con.close()

    assert user_events.event_id_exists(0) is True
    assert user_events.event_id_exists(1) is False
    clearDB()

def test_get_event():
    clearDB()
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    # Add test data to the database
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (0, 0, 1234567890, "description", "assignment", "HW1", 1);')
    con.commit()
    con.close()

    dict = user_events.get_event(0)
    assert dict == {'result': (0, 0, 1234567890, "description", "assignment", "HW1", None, None, 1, None, None, None)}

    dict = user_events.get_event(1)
    assert dict == {'result': 'event not found'}
    clearDB()

def test_get_usr_events():
    clearDB()
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    # Add test data to the database
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (0, 0, 1234567890, "description", "assignment", "HW1", 1);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (0, 1, 1234567890, "description", "assignment", "HW2", 1);')
    con.commit()
    con.close()

    dict = user_events.get_usr_events(0)
    assert dict == {'result': [(0, 0, 1234567890, "description", "assignment", "HW1", None, None, 1, None, None, None), (0, 1, 1234567890, "description", "assignment", "HW2", None, None, 1, None, None, None)]}

    dict = user_events.get_usr_events(1)
    assert dict == {'result': 'usr_id not found'}
    clearDB()

def test_create_event():
    clearDB()

    con = sqlite3.connect('server/usrDatabase/usrDB.db')
    dict = user_events.create_event(0, "description", "assignment", "HW1", None, 1707550546, 0, None, 1, None)
    assert dict == {'result': 'id not found'}

    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    con.commit()
    con.close()

    dict = user_events.create_event(0, "description", "assignment", "HW1", None, 1707550546, 0, None, 1, None)
    assert dict == {'result': 'event created'}

    # Ensure event was acutually added to db
    dict = user_events.get_event(0)
    assert 'result' in dict
    event_result = dict['result']
    assert isinstance(event_result[2], float) #make sure timestamp was added as float
    assert dict == {'result': (0, 0, event_result[2], "description", "assignment", "HW1", None, 1707550546, 0, None, 1, None)}

    clearDB()

def test_update_event():
    clearDB()
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    # Add test data to the database
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (0, 0, 1234567890, "description", "assignment", "HW1", 1);')
    con.commit()
    con.close()

    dict = user_events.update_event(0, "newTitle" , "newdesc", "lecture", None, None, 1, None, 0, 0)
    assert dict == {'result': 'event updated'}

    dict = user_events.get_event(0)
    assert dict == {'result': (0, 0, 1234567890, "newdesc", "lecture", "newTitle", None, None, 1, None, 0, 0)}
    clearDB()
    
def test_delete_event():
    clearDB()
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    # Add test data to the database
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (0, 0, 1234567890, "description", "assignment", "HW1", 1);')
    con.commit()
    con.close()

    dict = user_events.get_event(0)
    assert dict == {'result': (0, 0, 1234567890, "description", "assignment", "HW1", None, None, 1, None, None, None)}

    dict = user_events.delete_event(1)
    assert dict == {'result': 'event_id not found'}

    dict = user_events.delete_event(0)
    assert dict == {'result': 'event_id deleted'}

    dict = user_events.get_event(0)
    assert dict == {'result': 'event not found'}
