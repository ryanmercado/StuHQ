import React, { useState } from 'react';
import GroceryList from './GroceryList';
import RecipeList from './RecipeList';
import StockList from './StockList';
import { Link } from 'react-router-dom';

const RecipeLanding = () => {
    return (
        <div>
            <h1>Recipe Landing</h1>
            <div>
                <Link to="/grocery-list">Grocery List</Link>
            </div>
            <div>
                <Link to="/stock-list">Stock List</Link>
            </div>
            <div>
                <Link to="/recipe-list">Recipe List</Link>
            </div>
        </div>
    );
};


export default RecipeLanding;

