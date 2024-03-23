from calendar_module.canvasAPI import getData
from calendar_module import user_events
from flask import jsonify
'''
Data that needs to be gained from event JSON

created_epoch: will likely just be a timestamp for when the item is created
               in the DB
        -might not be useful
        -when the event is created in the DB

event_desc: availible in Canvas JSONs (description)

event_type: Assignment/Non-assignment? Or are we including things like
            lectures/OH/tests

event_title: availible in Canvas JSONs (name)

start_epoch: are we including this for assignments or just for other events
    -null for assignments

end_epoch: there is a due_at field in JSON files

is_submitted: availible in Canvas JSONs (has_submitted_submissions)

on_to_do_list: y/n should event show on to do list

want_notifications: y/n should user get a reminder about this event

???????????? Things I am not sure of their purpose ?????????????
 extra_data, want_notification

'''

def parseCanvasAssignments(usr_id, token):
    data = getData.getUpcomingAssignments(token)
    filtered_data = [{'course_id': assignment.get('course_id'), 
                      'description': assignment.get('description'), 
                      'name': assignment.get('name'), 
                      'due_at': assignment.get('due_at')} 
                      for assignment in data]
    
    for assignment in filtered_data:
        course_id = assignment.get('course_id')
        course = getData.getCourse(id=course_id, token=token)
        course_name = course.get('name')
        name = course_name + ': ' + assignment.get('name')
        print(course_name)
        user_events.create_event(usr_id=usr_id, 
                                 event_desc= assignment.get('description'), 
                                 event_type='Assignment', 
                                 event_title=name, 
                                 end_epoch=assignment.get('due_at'),
                                )
    
    return jsonify({'result': 'import successful'})