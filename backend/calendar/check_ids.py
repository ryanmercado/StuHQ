
class UserNotFoundException(Exception):
    pass
class EventNotFoundException(Exception):
    pass


def usr_id_exists(usr_id):
    con = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = con.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM calendar WHERE usr_id = ?', (usr_id,))
    count = cursor.fetchone()[0]
    
    con.close()

    return count > 0

def event_id_exists(event_id):
    con = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = con.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM calendar WHERE event_id = ?', (event_id,))
    count = cursor.fetchone()[0]
    
    con.close()

    return count > 0