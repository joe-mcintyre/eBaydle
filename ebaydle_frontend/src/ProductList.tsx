import React, { useState, useEffect } from 'react';
import { getProducts } from './services/api';

interface Product {
    name: string;
    price_original: number;
    url: string;
    photos: string[];
    seller_name: string;
    _id: string;
}

const ProductList: React.FC = () => {
    const [Products, setProducts] = useState<Product[]>([]);
    const [Loading, setLoading] = useState(true);

    useEffect(() => {
        const returnProducts = async () => {
            try {
                const { data } = await getProducts();
                setProducts(data);
            } catch (error) {
                console.error("Error retrieving products: ", error);
                //console.error("Error retrieving products: ", error.response?data || error.message);
            } finally {
                setLoading(false);
            }
        };

        returnProducts();
    }, []);


    if (Loading) return <p>Loading...</p>;

    return (
        <div>
            <h1>Product List</h1>
            <ul>
                {Products.map((product) => (
                    <li key={product._id}>
                        <h2>{product.name}</h2>
                        <p>Price: ${product.price_original}</p>
                        <a href={product.url}>Link to product</a>
                        <p>Seller: {product.seller_name}</p>
                        {product.photos.map((photo, index) => (
                            <img key={index} src={photo} alt={`${product.name} image`} />
                        ))}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ProductList;
