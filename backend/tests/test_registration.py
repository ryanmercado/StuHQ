import sqlite3
from backend import handleCreateAccount
import pytest

@pytest.fixture
def setup_teardown():
    clear_usr_db()
    res = handleCreateAccount.sign_up('Jaxon5', 'yayjaxon@gmail.com', 'TimeGrudge3!', 'TimeGrudge3!')
    assert (res['results'] == 'Account created successfully')



def clear_usr_db():

    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM usr_info')

    conn.commit()
    conn.close()
    
    
