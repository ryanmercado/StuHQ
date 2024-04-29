import React, { useState, useEffect, useRef } from 'react';
import { Calendar, Navigate, dayjsLocalizer } from 'react-big-calendar';
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
import '../assets/styles/Global.css';

function truncate(str){
    if (str.length <= 27) {
      return str;
    } else {
      return str.slice(0, 27) + '...'; 
    }
}

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
    const [isAddOpen, setAddOpen] = useState(false);
    const [isCanvasOpen, setCanvasOpen] = useState(false);
    const [canvas_token, setCanvasToken] = useState('')
    const [allEvents, setAllEvents] = useState(new Array);
    const [error, setError] = useState('');
    const calendarRef = useRef(null);
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
        console.log(event[6])

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
          if (xhr.status === 200) { 
            const response = JSON.parse(xhr.response)
          }
        };
        xhr.send(jsonData);
        setAddEvent({ title: "", start: null, end: null, description: "", eventType: "", on_to_do_list: false,});
        setStartDate(null);
        setEndDate(null);
        setStartTime(null);
        setEndTime(null);
        setTimeout(() => {
            fetchUserEvents();
        }, 1000);    
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
          if (xhr.status === 200) { 
            const response = JSON.parse(xhr.response)
          }
        };
        xhr.send(jsonData);
        eventIds.delete(event1.event_id)
        const updatedEvents = allEvents.filter((event) => event1.event_id !== event.event_id);
        setAllEvents(updatedEvents);
        setTimeout(() => {
            fetchUserEvents();
        }, 1000);   
     };

    const locales = {
        "en-US": require("date-fns/locale/en-US")
    };

    const handleOpenAdd = () => {
        setAddOpen(true)
    };

    const handleCloseAdd = () => {
        setAddEvent({ title: "", start: null, end: null, description: "", eventType: "", on_to_do_list: false,});
        setStartDate(null);
        setEndDate(null);
        setStartTime(null);
        setEndTime(null);
        setAddOpen(false)
    };
    
    const handleOpenCanvas = () => {
        setCanvasOpen(true)
    };
    
    const handleCloseCanvas = () => {
        setCanvasOpen(false)
    };
    const handleCanvasImport = () =>{
        const jsonData = JSON.stringify({ 'usr_id': usr_id , 'token': canvas_token});
        const xhr = new XMLHttpRequest();
        xhr.open("POST", `http://localhost:5000/api/canvasImport`, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onload = () => {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.response);
            }        
          }
        xhr.send(jsonData);
        setCanvasToken('')
        setTimeout(() => {
            fetchUserEvents();
        }, 1000);   
    };

    const handleSelectEvent = (event) => {
        setPopoverFields({
            title: event.title,
            start: event.start,
            end: event.end,
            desc : event.description,
            type : event.type,
            event: event
        })
        setAnchorEl(event.target);
        setPopoverOpen(true)
    };

    const handleClosePopover = () => {
        setAnchorEl(null);
        setPopoverOpen(false)
    };
    const handleCheckboxChange = () => {
        setAddEvent({ ...addEvent, on_to_do_list: !addEvent.on_to_do_list });
    };

    const localizer = dayjsLocalizer(dayjs);

    useEffect(() => {
        if (usr_id === null) {
            navigate("/");
        }
        loadFlag = !loadFlag
        fetchUserEvents();
    }, [usr_id, navigate]);

    return (
        <div>
            <div className='calendar-header'>
                <h1>Calendar</h1>
                <div className='button-container'>
                    <button className=' calendar-button' onClick={handleOpenAdd}>
                        Add Event
                    </button>
                    <button className=' calendar-button' onClick={handleOpenCanvas}>
                        Import Canvas Events
                    </button>
                </div>
            </div>
            <div>
        <Popover
             open={isCanvasOpen}
             anchorEl={calendarRef.current}
             onClose={handleCloseCanvas}
             transformOrigin={{
                 vertical: 'center',
                 horizontal: 'center',
                 }}
             anchorOrigin={{
                 vertical: 'center',
                 horizontal: 'center',
             }}>
             <div className='add-event-popup'>
                <h2>Import Canvas Events (FOR DEMO PURPOSES ONLY)</h2>
                <input type='text' placeholder='Canvas OAuth Token' value={canvas_token} onChange={(e) => setCanvasToken(e.target.value)} />
                <button onClick={() => {handleCanvasImport(); handleCloseCanvas();}}>
                    Import Events
                </button>
                <button style={{ marginLeft: "10px" }} onClick={handleCloseCanvas}>
                    Close
                </button>
             </div>
        </Popover>
        <Popover
             open={isAddOpen}
             anchorEl={calendarRef.current}
             onClose={handleCloseAdd}
             transformOrigin={{
                 vertical: 'center',
                 horizontal: 'center',
                 }}
             anchorOrigin={{
                 vertical: 'center',
                 horizontal: 'center',
             }}
        >
        <div className = 'add-event-popup' style={{ maxWidth: '400px', padding: '20px' }}>
            <h2>Add New Event</h2>
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

          <div className='button-container'>
            <input
                    type='checkbox'
                    id='showOnTodoList'
                    checked={addEvent.on_to_do_list}
                    onChange={handleCheckboxChange}
                />
            <p htmlFor='showOnTodoList' className='checkbox-label'> Show on Todo List</p>
            <button onClick={() => {handleAddEvent(); handleCloseAdd();}}>
                Add Event
            </button>
            <button style={{ marginLeft: "10px" }} onClick={handleCloseAdd}>
                Close
            </button>
            {error && <div style={{ color: 'red' }}>{error}</div>}
           </div>
        </div>
            </Popover>
        </div>
        <div style={{zIndex: 1 }}>
        <div className="calendar-container">
            <Calendar
                localizer={localizer}
                events={allEvents}
                startAccessor="start"
                endAccessor="end"
                style={{ height: 650, width: 900, margin: "10px" }}
                showMultiDayTimes
                onSelectEvent={(event, target) => handleSelectEvent(event, target)}
                ref = {calendarRef}
            />
        </div>
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
            <div className='event-popup'>
                <h className='title'>{truncate(popoverFields.title)}</h>
                <Typography>
                Start: {popoverFields.start &&
                    `${popoverFields.start.toLocaleDateString()} ${popoverFields.start.toLocaleTimeString([], {hour: 'numeric', minute: '2-digit'})}`}
                </Typography>
                <Typography>
                End: {popoverFields.end &&
                    `${popoverFields.end.toLocaleDateString()} ${popoverFields.end.toLocaleTimeString([], {hour: 'numeric', minute: '2-digit'})}`}
                </Typography>
                <Typography style={{ wordWrap: 'break-word' }}>Description: {popoverFields.desc}</Typography>
                <Typography>Event Type: {popoverFields.type}</Typography>
                <button onClick={handleClosePopover}>Close Popup</button>
                <button onClick={() => {deleteEvent(popoverFields.event); 
                                        handleClosePopover();}}>Delete Event</button>
            </div>
        </Popover>
    </div>
    );
}

export default CalendarLand;