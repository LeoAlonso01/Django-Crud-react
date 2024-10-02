import axios from "axios";

const API_URL = "http://localhost:8000/products/api/v1/sales/";

export const getSales = async () => {
    const response = await axios.get(API_URL);
    return response.data;
    }

export const getSale = async (id) => {
    const response = await axios.get(`${API_URL}/${id}`);
    return response.data;
    }

export const createSale = async (sale) => { 
    const response = await axios.post(API_URL, sale);
    return response.data;
    }

export const updateSale = async (sale) => {
    const response = await axios.put(`${API_URL}/${sale.id}`, sale);
    return response.data;
    }

export const deleteSale = async (id) => {
    const response = await axios.delete(`${API_URL}/${id}`);
    return response.data;
    }


    
