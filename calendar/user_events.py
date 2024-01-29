import sqlite3
from datetime import datetime

# Connect to SQLite database
db_file_path = "StuHQ/server/usrDatabase/usrDB.db"
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

conn.commit()

def create_event(usr_id, event_id, created_epoch, event_desc, event_type, event_title, start_epoch, end_epoch, is_important, extra_data, is_submitted, want_notification):
    cursor.execute('''
        INSERT INTO Calendar (usr_id, event_id, created_epoch, event_desc, event_type, event_title, start_epoch, end_epoch, is_important, extra_data, is_submitted, want_notification)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (usr_id, event_id, created_epoch, event_desc, event_type, event_title, start_epoch, end_epoch, is_important, extra_data, is_submitted, want_notification))
    conn.commit()

def read_event(event_id):
    cursor.execute('SELECT * FROM Calendar WHERE event_id = ?', (event_id,))
    return cursor.fetchone()

def update_event(event_id, new_event_title):
    cursor.execute('UPDATE Calendar SET event_title = ? WHERE event_id = ?', (new_event_title, event_id))
    conn.commit()

def delete_event(event_id):
    cursor.execute('DELETE FROM Calendar WHERE event_id = ?', (event_id,))
    conn.commit()

# Example Usage:
# create_event(1, 101, datetime.now(), 'Meeting', 'Business', 'Team Meeting', 1643685600, 1643692800, True, 'Additional data', False, True)
# print(read_event(101))
# update_event(101, 'Updated Title')
# print(read_event(101))
# delete_event(101)

# Close the connection
conn.close()
