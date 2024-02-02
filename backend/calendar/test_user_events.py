import unittest
import sqlite3
from datetime import datetime
from user_events import create_event, read_event, update_event, delete_event

class TestUserEvents(unittest.TestCase):

    path = "/home/cdew/StuHQ/server/usrDatabase/usrDB.db"

    def erase_all_entries(self):
        try:
            conn = sqlite3.connect(self.path)
            cursor = conn.cursor()

            # Execute the DELETE statement without a WHERE clause to delete all rows
            cursor.execute("DELETE FROM Calendar")

            # Commit the changes and close the connection
            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            print(f"Error: {e}")

    def test_db(self):
        con = sqlite3.connect(self.path)
        self.assertIsNot(con, 0)
        curs = con.cursor()
        curs.execute("select all usr_id from Calendar")
        record = curs.fetchall()
        self.assertGreater(len(record), 0)
        curs.close()


    def test_create_event(self):
        self.erase_all_entries()
        con = sqlite3.connect(self.path)
        curs = con.cursor()
        create_event(1, 101, datetime.now(), 'Meeting', 'Business', 'Team Meeting', 1643685600, 1643692800, True, 'Additional data', False, True, con)
        result = read_event(101, con)
        self.assertIsNotNone(result)
        self.assertEqual(result[5], 'Team Meeting')  # Check if the event title is correct
        curs.close()

    def test_update_event(self):
        self.erase_all_entries()
        con = sqlite3.connect(self.path)
        curs = con.cursor()
        create_event(1, 101, datetime.now(), 'Meeting', 'Business', 'Team Meeting', 1643685600, 1643692800, True, 'Additional data', False, True, con)
        update_event(101, 'Updated Title', con)
        result = read_event(101, con)
        self.assertIsNotNone(result)
        self.assertEqual(result[5], 'Updated Title')  # Check if the event title is updated
        curs.close()

    def test_delete_event(self):
        self.erase_all_entries()
        con = sqlite3.connect(self.path)
        curs = con.cursor()
        create_event(1, 101, datetime.now(), 'Meeting', 'Business', 'Team Meeting', 1643685600, 1643692800, True, 'Additional data', False, True, con)
        delete_event(101, con)
        result = read_event(101, con)
        self.assertIsNone(result)  # Check if the event is deleted
        curs.close()

if __name__ == '__main__':
    unittest.main()
