// ScrollPane.js
import React, { useState, useEffect } from 'react';
import CalendarLand from './CalendarLand';
import ToDo from './ToDo';
import '../assets/styles/Calendar.css';
 


const ScrollPane = () => {

    const [events, setEvents] = useState(new Array);

    const handleEventChange = (newEvents) => {
        const newArrayEvents = Array.isArray(newEvents) ? newEvents : [newEvents];
        setEvents(newArrayEvents);
    };

    return (
        <div className = "life-container" style={{ overflowY: 'scroll', height: '100vh', border: '1px solid #ccc', padding: '10px' }}>
            <CalendarLand className = 'calendar' onEventChange={handleEventChange}  />
            <ToDo className = 'todo' events ={events}/>
        </div>
    );
};

export default ScrollPane;
