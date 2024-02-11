import sqlite3
import pytest
from backend import handleCreateAccount
from backend import handleSignIn
from flask import Flask

# Define a mock Flask app for testing
def create_test_app():
    app = Flask(__name__)
    # Add any necessary configuration or routes for your mock app
    return app

# Use this function to create a mock Flask app
app = create_test_app()

@pytest.fixture(scope='module')
def app_client():
    with app.app_context():
        yield app.test_client()


@pytest.fixture(scope='module')
def app_client():
    with app.app_context():
        yield app.test_client()

@pytest.fixture
def clear_db_fixture():
    yield
    clear_usr_db()

@pytest.fixture
def populate_db_fixture():
    add_user_db()
    yield
    clear_usr_db()
    

def add_user_db():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (?,?, ?, ?, ?)", (0, 'User',
        'pswd', 'user@email.com', 0 ))
    conn.commit()
    conn.close()

def clear_usr_db():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usr_info')
    conn.commit()
    conn.close()



def test_put_valid_usr_in_empty_db(clear_db_fixture, app_client):
    res = handleCreateAccount.sign_up('User1', 'user1@gmail.com', 'Password', 'Password')
    assert (res.json['result']== 'account created successfully')

def test_put_valid_usr_in_populated_db(populate_db_fixture, app_client):
    res = handleCreateAccount.sign_up('User2', 'user2@gmail.com', 'Password2', 'Password2')
    assert (res.json['result']== 'account created successfully')

def test_put_invalid_password(clear_db_fixture, app_client):
    res = handleCreateAccount.sign_up('User', 'user@gmail.com', 'Password', 'Password1')
    assert (res.json['result']== 'passwords do not match')

def test_put_existing_email(populate_db_fixture, app_client):
    res = handleCreateAccount.sign_up('User1', 'user@email.com', 'Password', 'Password')
    assert(res.json['result'] == 'a user has already signed up with this email')

def test_put_existing_username(populate_db_fixture, app_client):
    res = handleCreateAccount.sign_up('User', 'user@email.com', 'Password', 'Password')
    assert (res.json['result'] == 'username already exists')

def test_successful_login(populate_db_fixture, app_client):
    res = handleSignIn.login('User', 'pswd')
    assert (res.json['result'] == 'login successful')

def test_successful_login(populate_db_fixture, app_client):
    res = handleSignIn.login('User', 'not_pswd')
    assert (res.json['result'] == 'login failed')


    
    
