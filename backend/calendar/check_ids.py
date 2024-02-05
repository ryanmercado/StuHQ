import sqlite3

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
    
    cursor.execute('SELECT COUNT(*) FROM calendar WHERE usr_id = ?', (usr_id,))
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