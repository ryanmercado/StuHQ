// Calendar.js
import React, { useState, useEffect } from 'react';
import { Calendar, dateFnsLocalizer } from 'react-big-calendar';
import format from 'date-fns/format';
import parse from 'date-fns/format';
import startOfWeek from 'date-fns/startOfWeek';
import getDay from 'date-fns/getDay';
import DatePicker from 'react-datepicker';
import "react-big-calendar/lib/css/react-big-calendar.css";
import "react-datepicker/dist/react-datepicker.css";
import secureLocalStorage from 'react-secure-storage'


const events = [];

function CalendarLand() {
    const [newEvent, setNewEvent] = useState({ title: "", start: "", end: "" });
    const [allEvents, setAllEvents] = useState(events);
    const usr_id = secureLocalStorage.getItem("usr_id")

    const fetchUserEvents = () => {
        const jsonData = JSON.stringify({'usr_id' : usr_id})
        const xhr = new XMLHttpRequest();
        xhr.open("GET", `http://localhost:5000/api/getUserEvents?usr_id=${usr_id}`, true);
        xhr.setRequestHeader("Content-Type", "application/json"); 
        xhr.onload = () => {
          if (xhr.status === 200) { // Handle cases: username taken, pwds don't match, email taken
            const response = JSON.parse(xhr.response)
            console.log(response)
            console.log(usr_id)
          }
        };
        xhr.send(jsonData);
    }

    const handleAddEvent = () => {
        if (newEvent.title.trim() !== '') {
            setAllEvents([...allEvents, newEvent]);
            setNewEvent({ title: "", start: "", end: "" });
        }
    };

    const deleteEvent = (eventId) => {
        const updatedEvents = allEvents.filter((event) => eventId.title !== event.title);
        setAllEvents(updatedEvents);
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

    useEffect(() => {
        fetchUserEvents();
    }, []);

    return (
        <div>
            <h1>Calendar</h1>
            <h2>Add New Event</h2>
            <div>
                <input type='text' placeholder='Add Title' value={newEvent.title} onChange={(e) => setNewEvent({ ...newEvent, title: e.target.value })} />
                <DatePicker placeholderText='Start Date' style={{ marginRight: "10px" }} selected={newEvent.start} onChange={(start) => setNewEvent({ ...newEvent, start: start })} />
                <DatePicker placeholderText='End Date' selected={newEvent.end} onChange={(end) => setNewEvent({ ...newEvent, end: end })} />
                <button style={{ marginTOp: "10px" }} onClick={handleAddEvent}>
                    Add Event
                </button>
            </div>
            <div>
                <h2>Event List</h2>
                <ul>
                    {allEvents.map((event) => {
                        return (<li>{event.title}: {event.start.toString()} - {event.end.toString()} <button onClick={() => deleteEvent(event)}>Delete Event</button></li>
                        );
                    })}
                </ul>
            </div>
            <Calendar localizer={localizer} events={allEvents} startAccessor="start" endAccessor="end" style={{ height: 500, margin: "50px" }} />
        </div>
    );
}

export default CalendarLand;
