// StockList.js
import React, { useState, useEffect } from 'react';

const StockList = () => {
    const [stockItems, setStockItems] = useState([]);
    const [newItem, setNewItem] = useState({
        usr_id: 1, //replace with the actual user ID or fetch it dynamically
        name: ''
    });

    const fetchStockList = async () => {
        try {
            const response = await fetch(`http://localhost:5000/api/getStock?usr_id=${newItem.usr_id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                },
            });

            if (!response.ok) {
                throw new Error('Failed to fetch Stock List');
            }

            const data = await response.json();
            setStockItems(JSON.parse(data.result));
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
                body: JSON.stringify(newItem)
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
            usr_id: 1, //replace with the actual user ID or fetch it dynamically
            name: ''
        });
    };

    const removeItem = async (name) => {
        try {
            const response = await fetch('https://localhost:5000/api/removeStockItem', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ usr_id: newItem.usr_id, name })
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
        fetchStockList();
    }, [newItem.usr_id]);


    return (
        <div>
            <ul>
                {stockItems.map((item) => {
                    <li key={item.name}>
                        {item.name}{' '}
                        <button onClick={() => removeItem(item.name)}>Remove</button>
                    </li>
                })}
            </ul>
            <label>
                Add Item:
                <input type="text" name="new-item" value={newItem.name} placeholder='Stock Item' onChange={(e) => setNewItem({ ...newItem, name: e.target.value })} />
            </label>
            <button onClick={addItem}>Add Item</button>
        </div>
    );
};

export default StockList;
