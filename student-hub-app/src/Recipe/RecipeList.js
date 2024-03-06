// RecipeList.js
import React, { useEffect, useState } from 'react';
import secureLocalStorage from 'react-secure-storage';
import { useNavigate } from 'react-router-dom';
import './styles/recipeList.css';

const RecipeList = () => {
    const navigate = useNavigate();
    const usr_id = secureLocalStorage.getItem('usr_id');
    const [recipeItems, setRecipeItems] = useState([]);
    const [newRecipe, setNewRecipe] = useState({
        name: '',
        ingredients: [],
        measurements: [],
        steps: '',
    });
    const [showPopup, setShowPopup] = useState(false);
    const [selectedRecipe, setSelectedRecipe] = useState(null);

    const fetchRecipes = async () => {
        const apiUrl = new URL('http://localhost:5000/api/getRecipes');
        const params = new URLSearchParams;
        params.append('usr_id', usr_id);
        apiUrl.search = params.toString();

        try {
            const response = await fetch(apiUrl, {
                method: 'GET'
            });

            if (!response.ok) {
                throw new Error('Failed to fetch recipes');
            }

            const data = await response.json();

            if (data.result === 'id did not exist') {
                setRecipeItems([]);
            } else {
                setRecipeItems(data);
            }


        } catch (error) {
            console.error('Error fetching recipes:', error.message);
        }
    };

    const addRecipe = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/addRecipe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    usr_id: usr_id,
                    name: newRecipe.name,
                    ingredients: newRecipe.ingredients,
                    measurements: newRecipe.measurements,
                    steps: newRecipe.steps
                }),
            });

            if (!response.ok) {
                throw new Error('Failed to add recipe');
            }

            const data = await response.json();
            console.log(data.message); // Recipe created successfully

            // Fetch updated recipes after adding a new one
            fetchRecipes();
        } catch (error) {
            console.error('Error adding recipe:', error.message);
        }
        setNewRecipe({
            name: '',
            ingredients: [],
            measurements: [],
            steps: '',
        });
    };

    const removeRecipe = async (name) => {
        try {
            const response = await fetch('http://localhost:5000/api/removeRecipe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ usr_id: usr_id, name: name }),
            });

            if (!response.ok) {
                throw new Error('Failed to remove recipe');
            }

            const data = await response.json();
            console.log(data.message); // Recipe deleted successfully

            // Fetch updated recipes after removing one
            fetchRecipes();
        } catch (error) {
            console.error('Error removing recipe:', error.message);
        }
    };

    useEffect(() => {

        if (usr_id === null) {
            navigate("/");
        } else {
            fetchRecipes();
        }
    }, [usr_id, navigate]);


    const RecipePopup = ({ recipe, onClose }) => {
        return (
            <div className="recipe-popup">
                <h3>{recipe.name}</h3>
                <p><strong>Ingredients:</strong> {recipe.ingredients}</p>
                <p><strong>Measurements:</strong> {recipe.measurements}</p>
                <p><strong>Steps:</strong> {recipe.steps}</p>
                <button onClick={onClose}>Close</button>
            </div>
        );
    };

    return (
        
        <div className="recipe-list-container scrollable-page">
            <h2>Your Recipe List</h2>
            <ul className="recipe-items-list">
                {recipeItems.map((recipe) => (
                    <li key={recipe.name} className="recipe-item" onClick={() => {
                        setSelectedRecipe(recipe);
                        setShowPopup(true);
                    }}>
                        {recipe.name}{' '}
                        <button className="remove-recipe-button" onClick={(e) => {e.stopPropagation(); removeRecipe(recipe.name);}}>Remove</button>
                    </li>
                ))}
            </ul>

            <div className="add-recipe-container">
                <h2>Add a New Recipe</h2>
                <form>
                    <label>
                        Name:
                        <input
                            type="text"
                            placeholder="Recipe Name"
                            value={newRecipe.name}
                            onChange={(e) => setNewRecipe({ ...newRecipe, name: e.target.value })}
                        />
                    </label>
                    <label>
                        Ingredients:
                        <input
                            placeholder="Ingredients separated by commas"
                            value={newRecipe.ingredients}
                            onChange={(e) => setNewRecipe({ ...newRecipe, ingredients: e.target.value })}
                        />
                    </label>
                    <label>
                        Measurements:
                        <input
                            placeholder="Measurements separated by commas"
                            value={newRecipe.measurements}
                            onChange={(e) => setNewRecipe({ ...newRecipe, measurements: e.target.value })}
                        />
                    </label>
                    <label>
                        Steps:
                        <input
                            placeholder="Steps"
                            value={newRecipe.steps}
                            onChange={(e) => setNewRecipe({ ...newRecipe, steps: e.target.value })}
                        />
                    </label>
                    <button type="button" onClick={addRecipe}>
                        Add Recipe
                    </button>
                </form>
            </div>
            {showPopup && (
            <div className="popup-container">
                <div className="popup-overlay" onClick={() => setShowPopup(false)}></div>
                <RecipePopup recipe={selectedRecipe} onClose={() => setShowPopup(false)} />
            </div>
            )}
        </div>

    );
};

export default RecipeList;
