import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api/users';

// Obtener todos los usuarios
export const getAllUsers = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching users:', error);
    throw error;
  }
};

// Obtener un usuario por su ID
export const getUserById = async (id_user) => {
  try {
    const response = await axios.get(`${API_URL}/${id_user}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching user:', error);
    throw error;
  }
};

// Crear un nuevo usuario
export const createUser = async (userData) => {
  try {
    const response = await axios.post(API_URL, userData);
    return response.data;
  } catch (error) {
    console.error('Error creating user:', error);
    throw error;
  }
};

// Actualizar un usuario existente
export const updateUser = async (id_user, userData) => {
  try {
    const response = await axios.put(`${API_URL}/${id_user}`, userData);
    return response.data;
  } catch (error) {
    console.error('Error updating user:', error);
    throw error;
  }
};

// Eliminar un usuario por su ID
export const deleteUser = async (id_user) => {
  try {
    const response = await axios.delete(`${API_URL}/${id_user}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting user:', error);
    throw error;
  }
};
