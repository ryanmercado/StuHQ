import sqlite3
from backend.calendar_module import user_events
import pytest
from flask import Flask

# Define a mock Flask app for testing
def create_test_app():
    app = Flask(__name__)
    return app

# Use this function to create a mock Flask app
app = create_test_app()

@pytest.fixture(scope='module')
def app_client():
    with app.app_context():
        yield app.test_client()

@pytest.fixture
def clear_db_fixture():
    yield
    clearDB()

# Clears usr_info and calendar tables
def clearDB():
    con = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM usr_info')
    cursor.execute('DELETE FROM calendar')
    con.commit()
    con.close()

def test_get_event_id(clear_db_fixture, app_client):
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

def test_usr_id_exists(clear_db_fixture, app_client):
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    # Add test data to the database
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    con.commit()
    con.close()

    assert user_events.usr_id_exists(0) is True
    assert user_events.usr_id_exists(1) is False


def test_event_id_exists(clear_db_fixture, app_client):
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    # Add test data to the database
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (1, 0, 1234567890, "description", "assignment", "HW1", 1);')
    con.commit()
    con.close()

    assert user_events.event_id_exists(0) is True
    assert user_events.event_id_exists(1) is False

def test_get_event(clear_db_fixture, app_client):
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    # Add test data to the database
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (0, 0, 1234567890, "description", "assignment", "HW1", 1);')
    con.commit()
    con.close()

    res = user_events.get_event(0)
    assert res.json['result'] == [0, 0, 1234567890, "description", "assignment", "HW1", None, None, 1, None, None, None]

    res = user_events.get_event(1)
    assert res.json['result'] == 'event not found'

def test_get_usr_events(clear_db_fixture, app_client):
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    # Add test data to the database
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (0, 0, 1234567890, "description", "assignment", "HW1", 1);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (0, 1, 1234567890, "description", "assignment", "HW2", 1);')
    con.commit()
    con.close()

    res = user_events.get_usr_events(0)
    assert res.json['result'] == [[0, 0, 1234567890, "description", "assignment", "HW1", None, None, 1, None, None, None], [0, 1, 1234567890, "description", "assignment", "HW2", None, None, 1, None, None, None]]

    res = user_events.get_usr_events(1)
    assert res.json['result'] == 'usr_id not found'

def test_create_event(clear_db_fixture, app_client):
    con = sqlite3.connect('server/usrDatabase/usrDB.db')
    res = user_events.create_event(0, "description", "assignment", "HW1", None, 1707550546, 0, None, 1, None)
    assert res.json['result'] == 'id not found'

    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    con.commit()
    con.close()

    res = user_events.create_event(0, "description", "assignment", "HW1", None, 1707550546, 0, None, 1, None)
    assert res.json['result'] == 'event created'

    # Ensure event was acutually added to db
    res = user_events.get_event(0)
    assert isinstance(res.json['result'][2], float) #checks created_epoch

def test_update_event(clear_db_fixture, app_client):
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    # Add test data to the database
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (0, 0, 1234567890, "description", "assignment", "HW1", 1);')
    con.commit()
    con.close()

    res = user_events.update_event(0, "newTitle" , "newdesc", "lecture", None, None, 1, None, 0, 0)
    assert res.json['result'] == 'event updated'

    res = user_events.update_event(14, "newTitle" , "newdesc", "lecture", None, None, 1, None, 0, 0)
    assert res.json['result'] == 'event_id not found'

    res = user_events.get_event(0)
    assert res.json['result'] == [0, 0, 1234567890, "newdesc", "lecture", "newTitle", None, None, 1, None, 0, 0]

def test_delete_event(clear_db_fixture, app_client):
    con = sqlite3.connect('server/usrDatabase/usrDB.db')

    # Add test data to the database
    cursor = con.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (0, "Jax5", "asvdfsrgh32423r", "jax5@email.com", 1234567890);')
    cursor.execute('INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, on_to_do_list) VALUES (0, 0, 1234567890, "description", "assignment", "HW1", 1);')
    con.commit()
    con.close()

    res = user_events.get_event(0)
    assert res.json['result'] == [0, 0, 1234567890, "description", "assignment", "HW1", None, None, 1, None, None, None]

    res = user_events.delete_event(1)
    assert res.json['result'] == 'event_id not found'

    res = user_events.delete_event(0)
    assert res.json['result'] == 'event_id deleted'

    res = user_events.get_event(0)
    assert res.json['result'] == 'event not found'
