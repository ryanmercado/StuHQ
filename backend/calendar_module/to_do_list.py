from datetime import datetime, timedelta

from flask import jsonify
import user_events
import sqlite3


def add_to_list(usr_id, event_desc, event_type, event_title, start_epoch, end_epoch):

    '''
        precondition: 
            usr_id exists in db as INT, not NULL
            event_desc is TEXT, not NULL
            event_type is VARCHAR(50), not NULL
            event_title is VARCHAR(50), not NULL
            start_epoch is INT, can be NULL
            end_epoch is INT, can be NULL
            on_to_do_list is BOOLEAN, not NULL

        postcondition:
            creates a new event using create new event, setting the on_to_do_list value to true

        TODO:
            create event_id's so that they are unique
            still needs to be tested with a unit test

    '''

    return user_events.create_event(usr_id, event_desc, event_type, event_title, start_epoch, end_epoch, 1, None, None, None)

def get_todo_list(usr_id):

    '''
        precondition: 
            usr_id is present in the db as INT

        postcondition: 
            returns all of the events with on_to_do_list true and occuring in the next week

        TODO:
            still needs to be tested with a unit test
    '''

    con = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = con.cursor()
    next_week_datetime = datetime.now() + timedelta(days=7)
    if(user_events.usr_id_exists(usr_id)):
        query = """
            SELECT event_id, event_title, start_epoch
            FROM calendar
            WHERE usr_id = ? AND start_epoch >= ? AND start_epoch <= ? AND on_to_do_list = 1
            ORDER BY start_epoch
        """
        now_epoch = datetime.now().timestamp()
        next_week_epoch = next_week_datetime.timestamp()

        cursor.execute(query, (usr_id, now_epoch, next_week_epoch))

        result = cursor.fetchall()

        if result[0] > 0:
            to_do_list = result[0] 
            return jsonify({'to_do_list': to_do_list})
        else:
            return jsonify({'result': 'get to_do_list failed, events may be empty'})
    else:
        raise jsonify({'result': 'usr_id not found'})