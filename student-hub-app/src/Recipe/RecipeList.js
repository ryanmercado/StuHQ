// RecipeList.js
import React, { useEffect, useState } from 'react';

const RecipeList = () => {
    const [recipeItems, setRecipeItems] = useState([]);
    const [newRecipe, setNewRecipe] = useState({
        usr_id: 1, // Replace with the actual user ID or fetch it dynamically
        name: '',
        ingredients: [],
        measurements: [],
        steps: '',
    });

    const fetchRecipes = async () => {

        const xhr = new XMLHttpRequest();
        xhr.open("GET", `http://localhost:5000/api/getRecipes?usr_id=${newRecipe.usr_id}`);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onload = () => {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.response);
                setRecipeItems(response);
                console.log(response);

            }
        };
        xhr.send();

    };
    //     try {
    //         const response = await fetch(`http://localhost:5000/api/getRecipes?usr_id=${newRecipe.usr_id}`, {
    //             method: 'GET',
    //             headers: {
    //                 'Content-Type': 'application/json',
    //             },
    //         });

    //         if (!response.ok) {
    //             throw new Error('Failed to fetch recipes');
    //         }

    //         const data = await response.json();
    //         setRecipeItems(JSON.parse(data.result));
    //     } catch (error) {
    //         console.error('Error fetching recipes:', error.message);
    //     }
    // };


    const addRecipe = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/addRecipe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(newRecipe),
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
            usr_id: 1, // Replace with the actual user ID or fetch it dynamically
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
                body: JSON.stringify({ usr_id: newRecipe.usr_id, name }),
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
        fetchRecipes();
    }, [newRecipe.usr_id]);

    return (
        <div>
            <h2>Your Recipe List</h2>
            <ul>
                {recipeItems.map((recipe) => (
                    <li key={recipe.name}>
                        {recipe.name}{' '}
                        <button onClick={() => removeRecipe(recipe.name)}>Remove</button>
                    </li>
                ))}
            </ul>

            <div>
                <h2>Add a New Recipe</h2>
                <form>
                    <label>
                        Name:
                        <input
                            type="text"
                            value={newRecipe.name}
                            onChange={(e) => setNewRecipe({ ...newRecipe, name: e.target.value })}
                        />
                    </label>
                    <label>
                        Ingredients:
                        <input
                            type="text"
                            value={newRecipe.ingredients.join(', ')}
                            onChange={(e) => setNewRecipe({ ...newRecipe, ingredients: e.target.value.split(', ') })}
                        />
                    </label>
                    <label>
                        Measurements:
                        <input
                            type="text"
                            placeholder="EX: (300 g, 200 ml, 2 tsp)"
                            value={newRecipe.measurements}
                            onChange={(e) => {
                                const measurementsString = e.target.value;
                                const measurementsArray = measurementsString
                                    .split(', ')
                                    .map((item) => {
                                        const [amount, unit] = item.split(' ');
                                        return [parseInt(amount, 10), unit];
                                    })
                                    .filter((item) => !isNaN(item[0])); // Filter out invalid entries
                                setNewRecipe({ ...newRecipe, measurements: measurementsArray });
                            }}
                        />
                    </label>
                    <label>
                        Steps:
                        <input
                            type="text"
                            value={newRecipe.steps}
                            onChange={(e) => setNewRecipe({ ...newRecipe, steps: e.target.value })}
                        />
                    </label>
                    <button type="button" onClick={addRecipe}>
                        Add Recipe
                    </button>
                </form>
            </div>
        </div>
    );
};

export default RecipeList;
