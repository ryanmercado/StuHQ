// RecipeList.js
import React, { useState } from 'react';

const RecipeList = () => {
    const [recipeItems, setRecipeItems] = useState([]);
    const [newItem, setNewItem] = useState('');

    const handleAddItem = () => {
        if (newItem.trim() !== '') {
            setRecipeItems([...recipeItems, newItem]);
            setNewItem('');
        }
    };

    const handleRemoveItem = (index) => {
        const updatedItems = [...recipeItems];
        updatedItems.splice(index, 1);
        setRecipeItems(updatedItems);
    };

    return (
        <div>
            <h2>Recipe List</h2>
            <ul>
                {recipeItems.map((item, index) => (
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

export default RecipeList;
