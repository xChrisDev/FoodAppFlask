import axios from 'axios';

// Base URL de la API para recetas
const API_URL = 'http://127.0.0.1:5000/api/users';

// Obtener todas las recetas de un usuario
export const getAllRecipesByUser = async (id_user) => {
  try {
    const response = await axios.get(`${API_URL}/${id_user}/recipes`);
    return response.data;
  } catch (error) {
    console.error('Error fetching recipes:', error);
    throw error;
  }
};

// Obtener una receta específica de un usuario
export const getRecipeByUserAndId = async (id_user, id_recipe) => {
  try {
    const response = await axios.get(`${API_URL}/${id_user}/recipes/${id_recipe}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching recipe:', error);
    throw error;
  }
};

// Crear una nueva receta para un usuario
export const createRecipe = async (id_user, recipeData) => {
  try {
    const response = await axios.post(`${API_URL}/${id_user}/recipes`, recipeData);
    return response.data;
  } catch (error) {
    console.error('Error creating recipe:', error);
    throw error;
  }
};

// Actualizar una receta de un usuario
export const updateRecipe = async (id_user, id_recipe, recipeData) => {
  try {
    const response = await axios.put(`${API_URL}/${id_user}/recipes/${id_recipe}`, recipeData);
    return response.data;
  } catch (error) {
    console.error('Error updating recipe:', error);
    throw error;
  }
};

// Eliminar una receta de un usuario
export const deleteRecipe = async (id_user, id_recipe) => {
  try {
    const response = await axios.delete(`${API_URL}/${id_user}/recipes/${id_recipe}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting recipe:', error);
    throw error;
  }
};
