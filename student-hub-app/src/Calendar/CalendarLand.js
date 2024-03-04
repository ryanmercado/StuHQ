import React, { useState, useEffect, useEffect } from 'react';
import { Calendar, Navigate, datejsLocalizer } from 'react-big-calendar';
import format from 'date-fns/format';
import parse from 'date-fns/format';
import startOfWeek from 'date-fns/startOfWeek';
import getDay from 'date-fns/getDay';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import Popover from '@mui/material/Popover';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import "react-big-calendar/lib/css/react-big-calendar.css";
import "react-datepicker/dist/react-datepicker.css";
import { useNavigate } from 'react-router-dom';
import secureLocalStorage from 'react-secure-storage';
import dayjs from 'dayjs';




function CalendarLand( {onEventChange} ) {
    const [eventIds, setEventIds] = useState(new Set());
    const navigate = useNavigate();
    const [addEvent, setAddEvent] = useState({ title: "", start: null, end: null, description: "", eventType: "", on_to_do_list: false,});
    const [startDate, setStartDate] = useState(null);
    const [endDate, setEndDate] = useState(null);
    const [startTime, setStartTime] = useState(null);
    const [endTime, setEndTime] = useState(null);
    const [anchorEl, setAnchorEl] = useState(null);
    const [isPopoverOpen, setPopoverOpen] = useState(false);
    const [allEvents, setAllEvents] = useState(new Array);
    const [error, setError] = useState('');
    const usr_id = secureLocalStorage.getItem("usr_id");
    var loadFlag = true;
    const [popoverFields, setPopoverFields] = useState({
        title: '',
        start: '',
        end: '',
        desc : '',
        type: ''
    });

    const fetchUserEvents = () => {
        const jsonData = JSON.stringify({ 'usr_id': usr_id });
        const xhr = new XMLHttpRequest();
        xhr.open("GET", `http://localhost:5000/api/getUserEvents?usr_id=${usr_id}`, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onload = () => {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.response);
                var todo = new Array
                if(loadFlag){
                    const response_events = response.result;                
                    const builtEvents = response_events.map(buildEvent)
                    for(let i = 0; i < builtEvents.length; i++){
                        if (builtEvents[i].on_to_do_list == 1){
                            todo.push(builtEvents[i])
                        }
                        if(!eventIds.has(builtEvents[i].event_id) && builtEvents[i].start !== null && !builtEvents[i].end !== null){
                            setAllEvents((allEvents) => [...allEvents, builtEvents[i]]);
                            eventIds.add(builtEvents[i].event_id)
                        }
                    }
                    loadFlag = false
                    onEventChange(todo);
                }        
            }
        };
        xhr.send(jsonData);
    };

    const buildEvent = (event) => {
        const startDate = event[6] ? new Date(event[6]) : null;
        const endDate = event[7] ? new Date(event[7]) : null;

        const newEvent = {
            event_id: event[1],
            title: event[5],  
            start: startDate,
            end: endDate,
            description: event[3],
            on_to_do_list: event[8],
            type: event[4]
          };
 
        return newEvent;
    }

    const handleAddEvent = () => {
        
        if (
            addEvent.title === '' ||
            startDate === null ||
            endDate === null ||
            startTime === null ||
            endTime === null ||
            addEvent.description === '' ||
            addEvent.eventType === ''
        ) {
            // Set an error message
            setError('Please fill in all fields');
            return;
        }
        setError('')

        const startDateTime = new Date(startDate);
        startDateTime.setHours(startTime.getHours(), startTime.getMinutes(), 0, 0);
      
        const endDateTime = new Date(endDate);
        endDateTime.setHours(endTime.getHours(), endTime.getMinutes(), 0, 0);

        if(endDateTime < startTime){
            setError('End time must come after start time')
            return;
        }
        setError('')

        const newEvent = {
          title: addEvent.title,  
          start: startDateTime,
          end: endDateTime,
          description: addEvent.description,
          type: addEvent.eventType,
          on_to_do_list: addEvent.on_to_do_list
        };

        if (newEvent.title.trim() !== '') {
          setAddEvent({ title: "", start: null, end: null, description: "", eventType: addEvent.eventType}); // Clear fields after adding the event
        }
        const formData = {
            usr_id : secureLocalStorage.getItem('usr_id'),
            event_desc : newEvent.description,
            event_type : newEvent.type,
            event_title : newEvent.title,
            start_epoch : newEvent.start.getTime(),
            end_epoch : newEvent.end.getTime(),
            on_to_do_list : newEvent.on_to_do_list == true ? 1:0 ,
            extra_data : null,
            is_submitted : null,
            want_notification : null
        }
        const jsonData = JSON.stringify(formData)
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "http://localhost:5000/api/createEvent");
        xhr.setRequestHeader("Content-Type", "application/json"); 
        xhr.onload = () => {
          if (xhr.status === 200) { // Handle cases: username taken, pwds don't match, email taken
            const response = JSON.parse(xhr.response)
          }
        };
        xhr.send(jsonData);
        loadFlag = true;
        fetchUserEvents();
      };

    const deleteEvent = (event1) => {
        const formData = {
            event_id: event1.event_id
        }
        const jsonData = JSON.stringify(formData)
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "http://localhost:5000/api/deleteEvent");
        xhr.setRequestHeader("Content-Type", "application/json"); 
        xhr.onload = () => {
          if (xhr.status === 200) { // Handle cases: username taken, pwds don't match, email taken
            const response = JSON.parse(xhr.response)
          }
        };
        xhr.send(jsonData);
        eventIds.delete(event1.event_id)
        const updatedEvents = allEvents.filter((event) => event1.event_id !== event.event_id);
        setAllEvents(updatedEvents);
        loadFlag = true;
        setTimeout(() => {
            fetchUserEvents();
        }, 1000);
        //     fetchUserEvents();

    };

    const locales = {
        "en-US": require("date-fns/locale/en-US")
    };

    const localizer = dateFnsLocalizer({
        format,
        parse,
        startOfWeek,
        getDay,
        locales
    });



    return (
        <div>
            <h1>Calendar</h1>
            <div>
        <h2>Add New Event</h2>
        <div style={{ zIndex: 2 }}>
            <input type='text' placeholder='Add Title' value={addEvent.title} onChange={(e) => setAddEvent({ ...addEvent, title: e.target.value })} />
            <input type='text' placeholder='Add Description' value={addEvent.description} onChange={(e) => setAddEvent({ ...addEvent, description: e.target.value })} />
            <select id='type_dropdown' value={addEvent.eventType} onChange={(e) => setAddEvent({ ...addEvent, eventType: e.target.value })}>
                <option value="" disabled hidden>Select Event Type</option>
                <option value="Meeting">Meeting</option>   
                <option value="Appointment">Appointment</option>
                <option value="Task">Task</option>
                <option value="Other">Other</option>
            </select>
          <DatePicker
            selected={startDate}
            onChange={(date) => setStartDate(date)}
            placeholderText='Start Date'
            />
            <DatePicker
            selected={endDate}
            onChange={(date) => setEndDate(date)}
            placeholderText='End Date'
            />
            <DatePicker
            selected={startTime}
            onChange={(time) => setStartTime(time)}
            showTimeSelect
            showTimeSelectOnly
            timeIntervals={15}
            timeCaption="Time"
            dateFormat="h:mm aa"
            placeholderText='Start Time'
            />
            <DatePicker
            selected={endTime}
            onChange={(time) => setEndTime(time)}
            showTimeSelect
            showTimeSelectOnly
            timeIntervals={15}
            timeCaption="Time"
            dateFormat="h:mm aa"
            placeholderText='End Time'
            />
            <input
            type='checkbox'
            id='showOnTodoList'
            checked={addEvent.on_to_do_list}
            onChange={handleCheckboxChange}
            />
            <label htmlFor='showOnTodoList'>Show on Todo List</label>
          <button style={{ marginTop: "10px" }} onClick={handleAddEvent}>
            Add Event
          </button>
          {error && <div style={{ color: 'red' }}>{error}</div>}
          </div>
      </div>
            <div>
                <h2>Event List</h2>
                <ul>
                    {allEvents.map((event) => {
                        return (<li>{event.title}: {event.start.toString()} - {event.end.toString()} - {event.description} <button onClick={() => deleteEvent(event)}>Delete Event</button></li>);
                    })}
                </ul>
            </div>
            <div style={{zIndex: 1 }}>
            <Calendar
                localizer={localizer}
                events={allEvents}
                startAccessor="start"
                endAccessor="end"
                style={{ height: 500, margin: "50px" }}
                showMultiDayTimes
                onSelectEvent={(event, target) => handleSelectEvent(event, target)}
            />
            </div>
            <Popover
                open={isPopoverOpen}
                anchorEl={anchorEl}
                onClose={handleClosePopover}
                transformOrigin={{
                    vertical: 'center',
                    horizontal: 'center',
                  }}
                anchorOrigin={{
                    vertical: 'center',
                    horizontal: 'center',
                }}
            >
                <div style={{ maxWidth: '400px', padding: '20px' }}>
                    <Typography variant="h6">{popoverFields.title}</Typography>
                    <Typography>Start: {popoverFields.start?.toString()}</Typography>
                    <Typography>End: {popoverFields.end?.toString()}</Typography>
                    <Typography>Description: {popoverFields.desc}</Typography>
                    <Typography>Event Type: {popoverFields.type}</Typography>
                    <Button onClick={handleClosePopover}>Close Popup</Button>
                </div>
            </Popover>
        </div>
    );
}

export default CalendarLand;
