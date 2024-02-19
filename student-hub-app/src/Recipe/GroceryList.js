import React, { useEffect, useState } from 'react';


const GroceryList = () => {
    const [groceryItems, setGroceryItems] = useState([]);
    const [newItem, setNewItem] = useState({
        usr_id: 1, //replace with the actual user ID or fetch it dynamically
        name: ''
    });

    const fetchGroceryList = async () => {
        try {
            const response = await fetch(`http://localhost:5000/api/getGroceryList?usr_id=${newItem.usr_id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                },
            });

            if (!response.ok) {
                throw new Error('Failed to fetch Grocery List');
            }

            const data = await response.json();
            setGroceryItems(JSON.parse(data.result));
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
                body: JSON.stringify(newItem)
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
            usr_id: 1, //replace with the actual user ID or fetch it dynamically
            name: ''
        });
    };

    const removeItem = async (name) => {
        try {
            const response = await fetch('https://localhost:5000/api/removeGroceryListIngredient', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ usr_id: newItem.usr_id, name })
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
        fetchGroceryList();
    }, [newItem.usr_id]);


    return (
        <div>
            <ul>
                {groceryItems.map((item) => {
                    <li key={item.name}>
                        {item.name}{' '}
                        <button onClick={() => removeItem(item.name)}>Remove</button>
                    </li>
                })}
            </ul>
            <label>
                Add Item:
                <input type="text" name="new-item" value={newItem.name} placeholder='Grocery Item' onChange={(e) => setNewItem({ ...newItem, name: e.target.value })} />
            </label>
            <button onClick={addItem}>Add Item</button>
        </div>
    );
};

export default GroceryList;