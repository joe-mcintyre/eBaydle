import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:5000 '});

export const addProduct = (name: string, price: number) => API.post('/add-product', {name, price});
