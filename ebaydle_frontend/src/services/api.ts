import axios from 'axios';

const API = axios.create({ baseURL: 'http://localhost:5000'});
export const getProducts = () => API.get('/products')
export const getProduct = () => API.get('/rand_product')
export const getProductPrice = (productID: string) => API.post('/getPrice', {productID});

//export const addProduct = (name: string, price_original: number) => API.post('/', {name, price_original});
