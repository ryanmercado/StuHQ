// RecipeList.js
import React, { useEffect, useState } from 'react';
import secureLocalStorage from 'react-secure-storage';
import { Link, useNavigate } from 'react-router-dom';
import './styles/recipeList.css';
import '../assets/styles/Calendar.css';

function truncate(str){
    if (str.length <= 65) {
      return str;
    } else {
      return str.slice(0, 65) + '...'; 
    }
  }

const RecipeList = () => {
    const navigate = useNavigate();
    const usr_id = secureLocalStorage.getItem('usr_id');
    const [recipeItems, setRecipeItems] = useState([]);
    const [newRecipe, setNewRecipe] = useState({
        name: '',
        ingredients: [''],
        measurements: [''],
        steps: [''],
    });
    const [showRecipePopup, setShowRecipePopup] = useState(false);
    const [showAddRecipePopup, setShowAddRecipePopup] = useState(false);
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

            const updatedIngredients = newRecipe.ingredients.map(ingredient => ingredient + " secureAppendage");
            const updatedMeasurements = newRecipe.measurements.map(measurement => measurement + " secureAppendage");
            const updatedSteps = newRecipe.steps.map(step => step + " secureAppendage");

            const response = await fetch('http://localhost:5000/api/addRecipe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    usr_id: usr_id,
                    name: newRecipe.name,
                    ingredients: updatedIngredients,
                    measurements: updatedMeasurements,
                    steps: updatedSteps
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
            ingredients: [''],
            measurements: [''],
            steps: [''],
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
        const ingredients = recipe.ingredients.join('').split(' secureAppendage');
        const measurements = recipe.measurements.join('').split(' secureAppendage');
        const steps = recipe.steps.join('').split(' secureAppendage');
        ingredients.pop();
        measurements.pop();
        steps.pop();

        return (
            <div className="recipe-popup">
                <h3 className='white-text'>{recipe.name}</h3>
                <p className='white-text'><strong>Ingredients:</strong></p>
                <ol>
                    {ingredients.map((ingredient, index) => (
                        <li className='white-text' key={index}>{ingredient}, {measurements[index]}</li>
                    ))}
                </ol>
                <p className='white-text'> <strong>Steps:</strong></p>
                <ol>
                {steps.map((step, index) => (
                    <li className='white-text' wordWrap= 'break-word' key={index}>{step}</li>
                ))}
            </ol>
                <button className="button-close" onClick={onClose}>Close</button>
            </div>
        );
    };

    const handleSteps = () => {
        setNewRecipe(prevState => ({
            ...prevState,
            steps: [...prevState.steps, '']
        }));
    };

    const handleRemoveStep = (index) => {
        setNewRecipe(prevState => {
            const updatedSteps = prevState.steps.filter((_, i) => i !== index);
            return {
                ...prevState,
                steps: updatedSteps
            };
        });
    };

    const handleStepChange = (index, value) => {
        setNewRecipe(prevState => {
            const updatedRecipe = {...prevState};
            updatedRecipe.steps[index] = value;
            return updatedRecipe;
        });
    };

    const handleAddIngredient = () => {
        setNewRecipe(prevState => ({
            ...prevState,
            ingredients: [...prevState.ingredients, ''],
            measurements: [...prevState.measurements, '']
        }));
    };

    const handleRemoveIngredient = (index) => {
        setNewRecipe(prevState => {
            const updatedIngredients = prevState.ingredients.filter((_, i) => i !== index);
            const updatedMeasurements = prevState.measurements.filter((_, i) => i !== index);
        
            return {
                ...prevState,
                ingredients: updatedIngredients,
                measurements: updatedMeasurements
            };
            
        });
    };

    const handleIngredientChange = (index, value, type) => {
        setNewRecipe(prevState => {
            const updatedRecipe = { ...prevState };
            if(type === 'ingredient') {
                updatedRecipe.ingredients[index] = value;
            } else if (type === 'measurement') {
                updatedRecipe.measurements[index] = value;
            }
            return updatedRecipe;
        });
    };

    return (
        
        <div className="recipe-list-container scrollable-page ">
            <div className='link-buttons'>
                <Link to="/grocery-list" className="link-button-grocery">
                    <button>Grocery List</button>
                </Link>
                <Link to="/stock-list" className="link-button-stock">
                    <button>Stock List</button>
                </Link>
            </div>
            <h2>Your Recipe List</h2>
            <ul className="recipe-items-list">
                {recipeItems.map((recipe) => (
                    <li key={recipe.name} className="recipe-item" onClick={() => {
                        setSelectedRecipe(recipe);
                        setShowRecipePopup(true);
                    }}>
                        {truncate(recipe.name)}{' '}
                        <button className="remove-recipe-button" onClick={(e) => {e.stopPropagation(); removeRecipe(recipe.name);}}>Remove</button>
                    </li>
                ))}
            </ul>


            {showAddRecipePopup && (
                


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
                        Steps:
                    </label>
                    <label>
                        <div className="steps-list">
                            {newRecipe.steps.map((step, index) => (
                                <div key={index} className="step-row">
                                    <label>
                                        {index + 1} {')'}
                                    </label>
                                    <input
                                        placeholder="Step"
                                        value={step}
                                        onChange={(e) => handleStepChange(index, e.target.value)}
                                    />
                                    <button
                                        type="button"
                                        onClick={() => handleRemoveStep(index)}
                                    >
                                        X
                                    </button>
                                </div>
                            ))}
                        </div>
                        <button
                            type="button"
                            className='add-step-button'
                            onClick={() => handleSteps()}
                        >
                            Add Step
                        </button>
                    </label>
                    <label>
                        Ingredients and Measurements:
                    </label>
                    <label>
                        <div className="ingredient-list">
                            {newRecipe.ingredients.map((ingredient, index) => (
                                <div key={index} className="ingredient-row">
                                    <input
                                        placeholder="Ingredient"
                                        value={ingredient}
                                        onChange={(e) => handleIngredientChange(index, e.target.value, 'ingredient')}
                                    />

                                    <input
                                        placeholder="Measurement"
                                        value={newRecipe.measurements[index] || ''}
                                        onChange={(e) => handleIngredientChange(index, e.target.value, 'measurement')}
                                    />
                                    <button
                                        type="button"
                                        onClick={() => handleRemoveIngredient(index)}
                                    >
                                        X
                                    </button>
                                </div>
                            ))}
                        </div>
                        <button
                        type="button"
                        onClick={() => handleAddIngredient()}
                    >
                        Add Ingredient
                    </button>
                    </label>
                    
                    <button type="button" onClick={addRecipe}>
                        Add Recipe
                    </button>
                </form>
                <button onClick={() => setShowAddRecipePopup(false)}>Cancel</button>
            </div>




            )}
            
            {!showAddRecipePopup && <button className="create-recipe-button" onClick={() => setShowAddRecipePopup(true)}>Create Recipe</button>}
            

            {showRecipePopup && (
            <div className="popup-container">
                <div className="popup-overlay" onClick={() => setShowRecipePopup(false)}></div>
                <RecipePopup recipe={selectedRecipe} onClose={() => setShowRecipePopup(false)} />
            </div>
            )}
        </div>

    );
};

export default RecipeList;
