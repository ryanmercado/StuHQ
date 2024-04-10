// StockList.js
import React, { useState, useEffect } from 'react';
import secureLocalStorage from 'react-secure-storage';
import { useNavigate, Link } from 'react-router-dom';
import './styles/stockList.css';


function truncate(str){
    if (str.length <= 60) {
      return str;
    } else {
      return str.slice(0, 60) + '...'; 
    }
  }

const StockList = () => {
    const navigate = useNavigate();
    const usr_id = secureLocalStorage.getItem('usr_id');
    const [stockItems, setStockItems] = useState([]);
    const [newItem, setNewItem] = useState({
        name: ''
    });

    const fetchStockList = async () => {
        const apiUrl = new URL('http://localhost:5000/api/getStock');
        const params = new URLSearchParams;
        params.append('usr_id', usr_id);
        apiUrl.search = params.toString();

        try {
            const response = await fetch(apiUrl, {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error('Failed to fetch Stock List');
            }

            const data = await response.json();

            console.log(data);

            if (data.result === 'usr did not exist') {
                setStockItems([])
            } else {
                setStockItems(data.split(', '));
            }
        } catch (error) {
            console.error('Error fetching stock list:', error.message);
        }
    };

    const addItem = async () => {
        try {
            const response = await fetch(`http://localhost:5000/api/addStockItem`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ usr_id: usr_id, item: newItem.name })
            });

            if (!response.ok) {
                throw new Error('Failed to add stock item');
            }

            const data = await response.json();
            console.log(data.message); //is there a message?

            fetchStockList();
        } catch (error) {
            console.error('Error adding stock item:', error.message);
        }
        setNewItem({
            name: ''
        });
    };

    const removeItem = async (name) => {
        try {
            const response = await fetch('http://localhost:5000/api/removeStockItem', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ usr_id: usr_id, item: name })
            });

            if (!response.ok) {
                throw new Error('Failed to remove stock item');
            }

            const data = await response.json();
            console.log(data.message); //is there a message?

            fetchStockList();
        } catch (error) {
            console.error('Error removing stock item:', error.message);
        }
    };

    useEffect(() => {
        if (usr_id === null) {
            navigate("/");
        } else {
            fetchStockList();
        }
    }, [usr_id, navigate]);


    return (
        
        <div className="stock-list-container">
            <div className='link-buttons'>
            <Link to="/recipe-list" >
                    <button className="link-button-grocery" >Recipe List</button>
            </Link>
            <Link to="/grocery-list">
                    <button  className="link-button-grocery" >Grocery List</button>
            </Link>
            </div>
            <h2>Your Stock List</h2>
            <div className="add-item-container">
                <input
                    type="text"
                    name= "new-item"
                    className="add-item-input"
                    value={newItem.name}
                    placeholder="Add item to stock..."
                    onChange={(e) => setNewItem({ name: e.target.value })}
                />
                <button className="add-item-button" onClick={addItem}>Add</button>
            </div>
            <div className='big-box'>
                <ul className="grocery-items-list">
                    {stockItems.map((item, index) => (
                        <li key={index} className= "stock-item" >
                            <span>{truncate(item)}</span>
                            <button className="remove-item-button" onClick={() => removeItem(item)}>X</button>
                        </li>
                    ))}
                </ul>
            </div>
            
        </div>
    );
};

export default StockList;
