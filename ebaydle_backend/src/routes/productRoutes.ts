import { Router } from 'express';
import Product from '../models/productModel';

const router = Router();

router.post('/add-product', async (req, res) => {
    const { name, price } = req.body;
    try {
        const newProduct = new Product({name, price});
        await newProduct.save();
        res.status(201).send(newProduct);
    } catch (error) {
        res.status(500).send({ error: 'Product failed to be added'})
    }
});

export default router;
