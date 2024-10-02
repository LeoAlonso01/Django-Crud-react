import axios from 'axios';

const API_URL = "http://localhost:8000/products/api/v1/users/";

export const getUsers = async () => {
    const response = await axios.get(API_URL);
    return response.data;
    }

export const getUser = async (id) => {
    const response = await axios.get(`${API_URL}${id}/`);
    return response.data;
    }

export const createUser = async (data) => {
    const response = await axios.post(API_URL, data);
    return response.data;
    }

export const updateUser = async (id, data) => {
    const response = await axios.put(`${API_URL}${id}/`, data);
    return response.data;
    }

export const deleteUser = async (id) => {
    const response = await axios.delete(`${API_URL}${id}/`);
    return response.data;
    }