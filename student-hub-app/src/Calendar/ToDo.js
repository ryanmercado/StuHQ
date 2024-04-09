import React, { useState, useEffect } from 'react';
import secureLocalStorage from 'react-secure-storage';
import '../assets/styles/ToDo.css';


function truncate(str){
  if (str.length <= 25) {
    return str;
  } else {
    return str.slice(0, 25) + '...'; 
  }
}

const ToDo = ({ events }) => {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState({id : '', title: '', description: '', eventType: '', completed: false});
  const [error, setError] = useState('');
  const [removedTasks, setRemovedTasks] = useState(new Set());

  const usr_id = secureLocalStorage.getItem("usr_id");

  // Update tasks when events prop changes
  useEffect(() => {
    if(events){
        loadEvents(events)
    }
  }, [events]);

  const loadEvents = (events) => {
    console.log(removedTasks)
    if(events && events.length != 0){
        const sortedEvents = [...events].sort((a, b) => {
            if (a.end === null) return -1; // Place events with null end time at the beginning
            if (b.end === null) return 1;
            return a.end.getTime() - b.end.getTime();
          });
        const newTasks = sortedEvents.map((event) => {
          if (removedTasks.has(event.event_id)) {
            return null; 
          }
          return {
            id: event.event_id,
            title: event.title,
            description: event.description,
            completed: false,
          }
        });
        setTasks(newTasks);
        setRemovedTasks(new Set());
    }else{
        setTasks([])
        setRemovedTasks(new Set());
    }
  }

  const handleAddTask = () => {

    if (
        newTask.title.trim() === '' ||
        newTask.description.trim() === '' ||
        newTask.eventType === ''
    ) {
        setError('Please fill in all fields');
        return;
    }
    setError('')

    const jsonData = JSON.stringify({ 'usr_id': usr_id, 'event_title': newTask.title, 'event_desc': newTask.description,'on_to_do_list': 1, 'event_type': newTask.eventType });

    const xhrPromise = new Promise((resolve, reject) => {
      const xhr = new XMLHttpRequest();
      xhr.open("POST", `http://localhost:5000/api/ToDoCreateEvent`, true);
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onload = () => {
        if (xhr.status === 200) {
          const response = JSON.parse(xhr.response);
          resolve(response.event_id);
        } else {
          reject(new Error('XHR request failed')); 
        }
      };
      xhr.onerror = () => reject(new Error('Network Error')); 
      xhr.send(jsonData);
    });

    xhrPromise.then((id) => {
      const newTaskObject = {
        id: id, 
        title: newTask.title,
        description: newTask.description,
        eventType: newTask.eventType,
        completed: false,
      };

      setTasks((prevTasks) => [...prevTasks, newTaskObject]);
      setNewTask({ id: '', title: '', description: '', eventType: '', completed: false });
    }).catch((error) => {
      console.error(error);
    });

    };

  const handleToggleTask = (taskId) => {
    setTasks((prevTasks) =>
      prevTasks.map((task) =>
        task.id === taskId ? { ...task, completed: !task.completed } : task
      )
    );
  };

  const handleRemoveTask = (taskId) => {
    const newSet = new Set(removedTasks);
    newSet.add(taskId);
    setRemovedTasks(newSet);
    console.log(removedTasks)
    console.log(newSet)    


    const jsonData = JSON.stringify({'event_id': taskId});
    const xhr = new XMLHttpRequest();
    xhr.open("GET", `http://localhost:5000/api/getEventInformation?event_id=${taskId}`, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = () => {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.response);
            console.log(response.result)
            var time = response.result[6]    

            if(time != null){
              const jsonData1 = JSON.stringify({ 'usr_id': usr_id, 'event_id': taskId, 'on_to_do_list': 0});
              const xhr1 = new XMLHttpRequest();
              xhr1.open("POST", `http://localhost:5000//api/toggleToDo`, true);
              xhr1.setRequestHeader("Content-Type", "application/json");
              xhr1.onload = () => {
                  if (xhr1.status === 200) {
                      const response = JSON.parse(xhr.response);
                  }
              }        
              xhr1.send(jsonData1);
            }else{
              const jsonData2 = JSON.stringify({'event_id': taskId});
              const xhr2 = new XMLHttpRequest();
              xhr2.open("POST", "http://localhost:5000/api/deleteEvent");
              xhr2.setRequestHeader("Content-Type", "application/json"); 
              xhr2.onload = () => {
                if (xhr2.status === 200) { 
                  const response = JSON.parse(xhr.response)
                }
              };
              xhr2.send(jsonData2);
            }
        }
        setTasks((prevTasks) => prevTasks.filter((task) => task.id !== taskId));
    }
    xhr.send(jsonData);
  };


  return (
    <div>
      <div className='todo-header'>
        <h1>Todo List</h1>
        <div className='todo-fields'>
        <input
          type="text"
          placeholder="Enter a new task"
          value={newTask.title}
          onChange={(e) => setNewTask({ ...newTask, title: e.target.value })}
        />
        <input
          type="text"
          placeholder="Enter a description"
          value={newTask.description}
          onChange={(e) => setNewTask({ ...newTask, description: e.target.value })}
        />
          <select id='type_dropdown' value={newTask.eventType} onChange={(e) => setNewTask({ ...newTask, eventType: e.target.value })}>
                <option value="" disabled hidden>Select Event Type</option>
                <option value="Meeting">Meeting</option>   
                <option value="Appointment">Appointment</option>
                <option value="Task">Task</option>
                <option value="Other">Other</option>
            </select>
        <button className='button' onClick={handleAddTask}>Add Task</button>
        </div>
        {error && <div className='error'>{error}</div>}
      </div>
      <ul className='task-list'>
        {tasks.map((task) => (
          <li key={task.id}>
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() => handleToggleTask(task.id)}
            />
            <span style={{textDecoration: task.completed ? 'line-through' : 'none' }}>
              {truncate(task.title)}
            </span>
            <button onClick={() => handleRemoveTask(task.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ToDo;
