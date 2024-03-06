import React, { useEffect } from 'react';
import GroceryList from './GroceryList';
import RecipeList from './RecipeList';
import StockList from './StockList';
import { Link, useNavigate } from 'react-router-dom';
import secureLocalStorage from 'react-secure-storage';
import './styles/recipeLanding.css';

const RecipeLanding = () => {
    const usr_id = secureLocalStorage.getItem('usr_id');
    const navigate = useNavigate();

    useEffect(() => {
        if (usr_id === null) {
            navigate("/");
        }
    }, [usr_id, navigate]);

    return (
        <div className="recipe-landing">
            <div className="content">
                <h1>Welcome to the Recipe Hub</h1>
                <div className="button-container">
                    <Link to="/grocery-list" className="button">Grocery List</Link>
                    <Link to="/stock-list" className="button">Stock List</Link>
                    <Link to="/recipe-list" className="button">Recipe List</Link>
                </div>
            </div>
        </div>
    );
};


export default RecipeLanding;

