import React, { useState, useEffect } from 'react';
import secureLocalStorage from 'react-secure-storage';
import '../assets/styles/ToDo.css';



const ToDo = ({ events }) => {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState({id : '', title: '', description: '', eventType: '', completed: false});
  const [error, setError] = useState('');
  const usr_id = secureLocalStorage.getItem("usr_id");

  // Update tasks when events prop changes
  useEffect(() => {
    if(events){
        loadEvents(events)
    }
  }, [events]);

  const loadEvents = (events) => {
    if(events && events.length != 0){
        const sortedEvents = [...events].sort((a, b) => {
            if (a.end === null) return -1; // Place events with null end time at the beginning
            if (b.end === null) return 1;
            return a.end.getTime() - b.end.getTime();
          });
        const newTasks = sortedEvents.map((event) => ({
          id: event.event_id,
          title: event.title,
          description: event.description,
          completed: false,
        }));
        setTasks(newTasks);
    }
  }

  const handleAddTask = () => {

    console.log(newTask)

    if (
        newTask.title.trim() === '' ||
        newTask.description.trim() === '' ||
        newTask.eventType === ''
    ) {
        // Set an error message
        setError('Please fill in all fields');
        return;
    }
    setError('')

    const jsonData = JSON.stringify({ 'usr_id': usr_id, 'event_title': newTask.title, 'event_desc': newTask.description,'on_to_do_list': 1, 'event_type': newTask.eventType});
    const xhr = new XMLHttpRequest();
    xhr.open("POST", `http://localhost:5000//api/ToDoCreateEvent`, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = () => {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.response);
            console.log(response)
        }
    }        
    xhr.send(jsonData);
    const newTaskObject = {
        id: Date.now(), // Generate a unique ID (you can use a library like uuid for more robust IDs)
        title: newTask.title,
        description: newTask.description,
        eventType: newTask.eventType,
        completed: false,
      };
  
    setTasks((prevTasks) => [...prevTasks, newTaskObject]);
    setNewTask({ id: '', title: '', description: '', eventType: newTask.eventType, completed: false });

    };

  const handleToggleTask = (taskId) => {
    setTasks((prevTasks) =>
      prevTasks.map((task) =>
        task.id === taskId ? { ...task, completed: !task.completed } : task
      )
    );
  };

  const handleRemoveTask = (taskId) => {
    const jsonData = JSON.stringify({ 'usr_id': usr_id, 'event_id': taskId, 'on_to_do_list': 0});
    console.log(jsonData)
    const xhr = new XMLHttpRequest();
    xhr.open("POST", `http://localhost:5000//api/toggleToDo`, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = () => {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.response);
            setTasks((prevTasks) => prevTasks.filter((task) => task.id !== taskId));
        }
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
            <span style={{ textDecoration: task.completed ? 'line-through' : 'none' }}>
              {task.title}
            </span>
            <button onClick={() => handleRemoveTask(task.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ToDo;
