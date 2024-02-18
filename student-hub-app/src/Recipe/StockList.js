// StockList.js
import React, { useState } from 'react';

const StockList = () => {
    const [stockItems, setStockItems] = useState([]);
    const [newItem, setNewItem] = useState('');

    const handleAddItem = () => {
        if (newItem.trim() !== '') {
            setStockItems([...stockItems, newItem]);
            setNewItem('');
        }
    };

    const handleRemoveItem = (index) => {
        const updatedItems = [...stockItems];
        updatedItems.splice(index, 1);
        setStockItems(updatedItems);
    };

    return (
        <div>
            <h2>Stock List</h2>
            <ul>
                {stockItems.map((item, index) => (
                    <li key={index}>
                        {item}
                        <button onClick={() => handleRemoveItem(index)}>Remove</button>
                    </li>
                ))}
            </ul>
            <div>
                <input
                    type="text"
                    value={newItem}
                    onChange={(e) => setNewItem(e.target.value)}
                />
                <button onClick={handleAddItem}>Add Item</button>
            </div>
        </div>
    );
};

export default StockList;
