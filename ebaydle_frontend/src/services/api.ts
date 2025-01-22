import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:5000'});
export const getProducts = () => API.get('/products')

//export const addProduct = (name: string, price_original: number) => API.post('/', {name, price_original});
