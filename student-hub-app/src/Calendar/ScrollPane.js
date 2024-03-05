// ScrollPane.js
import React, { useState, useEffect } from 'react';
import CalendarLand from './CalendarLand';
import ToDo from './ToDo';


const ScrollPane = () => {

    const [events, setEvents] = useState(new Array);

    const handleEventChange = (newEvents) => {
        const newArrayEvents = Array.isArray(newEvents) ? newEvents : [newEvents];
        setEvents(newArrayEvents);
    };

    return (
        <div style={{ overflowY: 'scroll', height: '100vh', border: '1px solid #ccc', padding: '10px' }}>
            <CalendarLand onEventChange={handleEventChange}  />
            <ToDo events ={events}/>
        </div>
    );
};

export default ScrollPane;
