import React, { useEffect, useState } from 'react';
import secureLocalStorage from 'react-secure-storage';
import { useNavigate } from 'react-router-dom';


const GroceryList = () => {
    const navigate = useNavigate();
    const usr_id = secureLocalStorage.getItem('usr_id');
    const [groceryItems, setGroceryItems] = useState([]);
    const [newItem, setNewItem] = useState({
        name: ''
    });

    const fetchGroceryList = async () => {
        const apiUrl = new URL('http://localhost:5000/api/getGroceryList');
        const params = new URLSearchParams;
        params.append('usr_id', usr_id);
        apiUrl.search = params.toString();

        try {
            const response = await fetch(apiUrl, {
                method: 'GET'
            });

            if (!response.ok) {
                throw new Error('Failed to fetch Grocery List');
            }

            const data = await response.json();

            if (data.result === 'id did not exist') {
                setGroceryItems([]);
            } else {
                setGroceryItems(data.split(', '));
            }
        } catch (error) {
            console.error('Error fetching grocery list:', error.message);
        }


    };

    const addItem = async () => {
        try {
            const response = await fetch(`http://localhost:5000/api/addGroceryListIngredient`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ usr_id: usr_id, item: newItem.name })
            });

            if (!response.ok) {
                throw new Error('Failed to add grocery item');
            }

            const data = await response.json();
            console.log(data.message); //is there a message?

            fetchGroceryList();
        } catch (error) {
            console.error('Error adding grocery item:', error.message);
        }
        setNewItem({
            name: ''
        });
    };

    const removeItem = async (name) => {
        try {
            const response = await fetch('http://localhost:5000/api/removeGroceryListIngredient', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ usr_id: usr_id, item: name })
            });

            if (!response.ok) {
                throw new Error('Failed to remove grocery item');
            }

            const data = await response.json();
            console.log(data.message); //is there a message?

            fetchGroceryList();
        } catch (error) {
            console.error('Error removing grocery item:', error.message);
        }
    };

    useEffect(() => {

        if (usr_id === null) {
            navigate("/");
        } else {
            fetchGroceryList();
        }
    }, [usr_id, navigate]);


    return (
        <div>
            <h2>Your Grocery List</h2>
            <ul>
                {
                    groceryItems.map((item, index) => (
                        <li key={index}>
                            {item}{' '}
                            <button onClick={() => removeItem(item)}>Remove</button>
                        </li>
                    ))
                }
            </ul>
            <label>
                Add Item:
                <input type="text" name="new-item" value={newItem.name} placeholder='Grocery Item' onChange={(e) => setNewItem({ name: e.target.value })} />
            </label>
            <button onClick={addItem}>Add Item</button>
        </div>
    );
};

export default GroceryList;