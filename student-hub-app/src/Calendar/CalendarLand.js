import React, { useState, useEffect } from 'react';
import { Calendar, dayjsLocalizer } from 'react-big-calendar';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import Popover from '@mui/material/Popover';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import "react-big-calendar/lib/css/react-big-calendar.css";
import "react-datepicker/dist/react-datepicker.css";
import secureLocalStorage from 'react-secure-storage';
import dayjs from 'dayjs'



const events = [];

function CalendarLand() {
    const [addEvent, setAddEvent] = useState({ title: "", start: null, end: null, description: "", eventType: "" });
    const [startDate, setStartDate] = useState(null);
    const [endDate, setEndDate] = useState(null);
    const [startTime, setStartTime] = useState(null);
    const [endTime, setEndTime] = useState(null);
    const [anchorEl, setAnchorEl] = useState(null);
    const [isPopoverOpen, setPopoverOpen] = useState(false);
    const [allEvents, setAllEvents] = useState(events);
    const [selectedEvent, setSelectedEvent] = useState(null);
    const usr_id = secureLocalStorage.getItem("usr_id");
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
            }
        };
        xhr.send(jsonData);
    };

    const handleAddEvent = () => {
        const startDateTime = new Date(startDate);
        startDateTime.setHours(startTime.getHours(), startTime.getMinutes(), 0, 0);
      
        const endDateTime = new Date(endDate);
        endDateTime.setHours(endTime.getHours(), endTime.getMinutes(), 0, 0);
      
        const newEvent = {
          title: addEvent.title,  
          start: startDateTime,
          end: endDateTime,
          description: addEvent.description,
          type: addEvent.eventType
        };
      
        if (newEvent.title.trim() !== '') {
          setAllEvents([...allEvents, newEvent]);
          setAddEvent({ title: "", start: null, end: null, description: "", eventType: null }); // Clear fields after adding the event
          console.log(newEvent);
        }
        const formData = {
            usr_id : secureLocalStorage.getItem('usr_id'),
            event_desc : newEvent.description,
            event_type : newEvent.type,
            event_title : newEvent.title,
            start_epoch : newEvent.start.getTime(),
            end_epoch : newEvent.end.getTime(),
            on_to_do_list : false,
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

      };

    const deleteEvent = (eventId) => {
        const updatedEvents = allEvents.filter((event) => eventId.title !== event.title);
        setAllEvents(updatedEvents);
    };

    const locales = {
        "en-US": require("date-fns/locale/en-US")
    };

    const handleSelectEvent = (event) => {
        console.log(event.eventType)
        setPopoverFields({
            title: event.title,
            start: event.start,
            end: event.end,
            desc : event.description,
            type : event.eventType
        })
        setAnchorEl(event.target);
        setPopoverOpen(true)
    };

    const handleClosePopover = () => {
        setAnchorEl(null);
        setPopoverOpen(false)
    };

    const open = Boolean(anchorEl);
    const localizer = dayjsLocalizer(dayjs);

    useEffect(() => {
        fetchUserEvents();
    }, []);

    return (
        <div>
            <h1>Calendar</h1>
            <div>
        <h2>Add New Event</h2>
        <div>
            <input type='text' placeholder='Add Title' value={addEvent.title} onChange={(e) => setAddEvent({ ...addEvent, title: e.target.value })} />
            <input type='text' placeholder='Add Description' value={addEvent.description} onChange={(e) => setAddEvent({ ...addEvent, description: e.target.value })} />
            <select value={addEvent.eventType} onChange={(e) => setAddEvent({ ...addEvent, eventType: e.target.value })}>
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
          <button style={{ marginTop: "10px" }} onClick={handleAddEvent}>
            Add Event
          </button>
        </div>
      </div>
            <div>
                <h2>Event List</h2>
                <ul>
                    {allEvents.map((event) => {
                        return (<li>{event.title}: {event.start.toString()} - {event.end.toString()} - {event.description} <button onClick={() => deleteEvent(event)}>Delete Event</button></li>
                        );
                    })}
                </ul>
            </div>
            <Calendar
                localizer={localizer}
                events={allEvents}
                startAccessor="start"
                endAccessor="end"
                style={{ height: 500, margin: "50px" }}
                showMultiDayTimes
                onSelectEvent={(event, target) => handleSelectEvent(event, target)}
            />
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
