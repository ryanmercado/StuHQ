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