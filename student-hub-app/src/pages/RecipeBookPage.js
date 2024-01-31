import React, { useState, useEffect } from 'react';
import "./../assets/styles/App.css"
import { useNavigate } from 'react-router-dom';


function RecipeBook() {
  const [recipes, setRecipes] = useState([]);
  const [newRecipeName, setNewRecipeName] = useState('');
  const [newRecipeIngredients, setNewRecipeIngredients] = useState('');

  useEffect(() => {
    // Fetch recipes from your Flask API endpoint
    fetch('http://localhost:5000/api/getRecipes')
      .then((response) => response.json())
      .then((data) => setRecipes(data.recipes))
      .catch((error) => console.error('Error fetching recipes:', error));
  }, []);

  const handleCreateRecipe = () => {
    // Send a POST request to create a new recipe
    fetch('http://localhost:5000/api/addRecipe', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: newRecipeName,
        ingredients: newRecipeIngredients.split(',').map((ingredient) => ingredient.trim()),
      }),
    })
      .then((response) => response.json())
      .then(() => {
        // Refresh the recipes list
        fetch('http://localhost:5000/api/getRecipes')
          .then((response) => response.json())
          .then((data) => setRecipes(data.recipes))
          .catch((error) => console.error('Error fetching recipes:', error));
      })
      .catch((error) => console.error('Error creating recipe:', error));
  };

//  const handleDeleteRecipe = (recipeId) => {
//    // Send a DELETE request to delete a recipe
//    fetch('/api/removeRecipe', {
//      method: 'POST',
//      headers: {
//        'Content-Type': 'application/json',
//      },
//      body: JSON.stringify({
//        name: newRecipeName,
//        ingredients: newRecipeIngredients.split(',').map((ingredient) => ingredient.trim()),
//      }),
//    })
//      .then(() => {
//        // Refresh the recipes list
//        fetch('/api/recipes')
//          .then((response) => response.json())
//          .then((data) => setRecipes(data.recipes))
//          .catch((error) => console.error('Error fetching recipes:', error));
//      })
//      .catch((error) => console.error('Error deleting recipe:', error));
//  };

//  const handleAddToGroceryList = (recipeId) => {
//    // Send a POST request to add a recipe to the grocery list
//    fetch('/api/add_recipe_to_grocery_list', {
//      method: 'POST',
//      headers: {
//        'Content-Type': 'application/json',
//      },
//      body: JSON.stringify({ recipeId }),
//    })
//      .then((response) => response.json())
//      .then(() => {
//        // Handle the success response as needed
//        // You can update the UI or show a confirmation message
//      })
//      .catch((error) => console.error('Error adding recipe to grocery list:', error));
//  };

  return (
    <div>
      <h1>Recipe Book</h1>
      <div>
        <h2>Create a Recipe</h2>
        <input
          type="text"
          placeholder="Recipe Name"
          value={newRecipeName}
          onChange={(e) => setNewRecipeName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Ingredients (comma-separated)"
          value={newRecipeIngredients}
          onChange={(e) => setNewRecipeIngredients(e.target.value)}
        />
        <button onClick={handleCreateRecipe}>Create Recipe</button>
      </div>
      <div>
        <h2>Recipes</h2>
        <ul>
          {recipes.map((recipe) => (
            <li key={recipe.id}>
              {recipe.name}
              <button>Delete</button>
              <button>Add to Grocery List</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default RecipeBook;