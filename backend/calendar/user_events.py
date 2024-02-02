import sqlite3
from datetime import datetime

# # Connect to SQLite database
# db_file_path = "/home/cdew/StuHQ/server/usrDatabase/test.db"
# conn = sqlite3.connect(db_file_path)
# cursor = conn.cursor()

# conn.commit()

def create_event(usr_id, event_id, created_epoch, event_desc, event_type, event_title, start_epoch, end_epoch, is_important, extra_data, is_submitted, want_notification, conn):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, start_epoch, end_epoch, is_important, extra_data, is_submitted, want_notification)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (usr_id, event_id, created_epoch, event_desc, event_type, event_title, start_epoch, end_epoch, is_important, extra_data, is_submitted, want_notification))
    conn.commit()

def read_event(event_id, conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM calendar WHERE event_id = ?', (event_id,))
    return cursor.fetchone()

def update_event(event_id, new_event_title, conn):
    cursor = conn.cursor()
    cursor.execute('UPDATE clendar SET event_title = ? WHERE event_id = ?', (new_event_title, event_id))
    conn.commit()

def delete_event(event_id, conn):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM calendar WHERE event_id = ?', (event_id,))
    conn.commit()


