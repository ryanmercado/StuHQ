import React, { useState } from 'react';

const GroceryList = () => {
    const [groceryItems, setGroceryItems] = useState([]);
    const [newItem, setNewItem] = useState('');

    const handleAddItem = () => {
        if (newItem.trim() !== '') {
            setGroceryItems([...groceryItems, newItem]);
            setNewItem('');
        }
    };

    const handleRemoveItem = (index) => {
        const updatedItems = [...groceryItems];
        updatedItems.splice(index, 1);
        setGroceryItems(updatedItems);
    };


    return (
        <div>
            <ul>
                {groceryItems.map((item, index) => {
                    return (
                        <li key={index}>
                            {item}
                            <button onClick={() => handleRemoveItem(index)}>Remove Item</button>
                        </li>);
                })}
            </ul>
            <label>
                Add Item:
                <input type="text" name="new-item" value={newItem} placeholder='Grocery Item' onChange={(e) => setNewItem(e.target.value)} />
            </label>
            <button onClick={handleAddItem}>Add Item</button>
        </div>
    );
};

export default GroceryList;