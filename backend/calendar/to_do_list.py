from datetime import datetime, timedelta
import user_events
import sqlite3


class ToDoList():

    todo = [] # contains all the events to be shown in list

    # NEED TO CHANGE IS_IMPORTANT 

    def get_todo_list(self, usr_id):
        self.todo = self.getList(usr_id)
        return self.todo
    
    def add_to_list(self,usr_id, event_desc, event_type, event_title, start_epoch, end_epoch, is_important):
        created_epoch = datetime.now().timestamp()
        user_events.create_event(usr_id, 1, created_epoch, event_desc, event_type, event_title, start_epoch, end_epoch, is_important)
        self.get_todo_list(usr_id)

    def getList(self, usr_id):
        con = sqlite3.connect('server/usrDatabase/usrDB.db')
        cursor = con.cursor()
        next_week_datetime = datetime.now() + timedelta(days=7)

        query = """
            SELECT event_id, event_title, start_epoch
            FROM calendar
            WHERE usr_id = ? AND start_epoch >= ? AND start_epoch <= ? AND is_important = 1
            ORDER BY start_epoch
        """
        now_epoch = datetime.now().timestamp()
        next_week_epoch = next_week_datetime.timestamp()

        cursor.execute(query, (usr_id, datetime.now(), next_week_epoch))

        result = cursor.fetchall()

        self.todo = result

        cursor.close()
        con.close()

