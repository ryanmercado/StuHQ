import React, { useEffect } from 'react';
import GroceryList from './GroceryList';
import RecipeList from './RecipeList';
import StockList from './StockList';
import { Link, useNavigate } from 'react-router-dom';
import secureLocalStorage from 'react-secure-storage';

const RecipeLanding = () => {
    const usr_id = secureLocalStorage.getItem('usr_id');
    const navigate = useNavigate();

    useEffect(() => {
        if (usr_id === null) {
            navigate("/");
        }
    }, [usr_id, navigate]);

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

