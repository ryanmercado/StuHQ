import React, { useEffect, useState } from 'react';
import secureLocalStorage from 'react-secure-storage';
import { useNavigate } from 'react-router-dom';
import './styles/groceryList.css';


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

    const purchasedItem = async (name) => {
        try {
            const response = await fetch('http://localhost:5000/api/purchasedIngredient', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ usr_id: usr_id, item: name })
            });

            if (!response.ok) {
                throw new Error('Failed to purchase item');
            }

            const data = await response.json();
            console.log(data.message);

            fetchGroceryList();
        } catch (error) {
            console.error('Error purchasing item: ', error.message);
        }
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
        <div className="grocery-list-container">
            <h2>Your Grocery List</h2>
            <div className="add-item-container">
                <input
                    type="text"
                    name= "new-item"
                    className="add-item-input"
                    value={newItem.name}
                    placeholder="Add new item..."
                    onChange={(e) => setNewItem({ name: e.target.value })}
                />
                <button className="add-item-button" onClick={addItem}>Add</button>
            </div>
            <div className='big-box'>
                <ul className="grocery-items-list">
                    {groceryItems.map((item, index) => (
                        <li key={index} className= "grocery-item" >
                            <div className='left-item'>
                                <span>{item}</span>
                            </div>
                            <div className='right-item'>
                                <button className="remove-item-b" onClick={() => removeItem(item)}>X</button>
                                <button className="purchased-button" onClick={() => purchasedItem(item)}>Purchased!</button>
                            </div>
                            
                        </li>
                    ))}
                </ul>
            </div>
            
        </div>
        
    );
};

export default GroceryList;