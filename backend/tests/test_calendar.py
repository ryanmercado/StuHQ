import sqlite3
from backend.calendar_module import check_ids
from backend import handleCreateAccount
import pytest

@pytest.fixture
def setup_teardown():
    # Setup
    handleCreateAccount.sign_up('Jaxon5', 'jaxon@gmail.com', 'TimeGrudge3!', 'TimeGrudge3!')
    yield
    # Teardown
    clearDB()

def test_usr_id_exists(setup_teardown):
    assert check_ids.usr_id_exists(0)
    assert not check_ids.usr_id_exists(34534)

# Uncomment the test_event_id_exists function when you're ready to implement it
# def test_event_id_exists():
#     # Test cases for event_id_exists function
#     assert event_id_exists("valid_event_id")
#     assert not event_id_exists("invalid_event_id")

def clearDB():
    con = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = con.cursor()

    cursor.execute('DELETE FROM usr_info')

    con.commit()
    con.close()
