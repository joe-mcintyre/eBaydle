import React, { useState, useEffect } from 'react';
import { getProduct } from './services/api';

interface Product {
    name: string;
    price_original: number;
    url: string;
    photos: string[];
    seller_name: string;
    _id: string;
}

const RandomProduct: React.FC = () => {
    const [product, setProduct] = useState<Product | undefined>();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const returnProduct = async() => {
            try {
                const { data } = await getProduct();
                setProduct(data);
            } catch (error) {
                console.error("Error retrieving product: ", error);
            } finally {
                setLoading(false);
            }
        };
        returnProduct();
    }, []);

    if (loading) return <p>Loading...</p>;
    if (!product) return <p>Error loading product. Please try again later.</p>;
    return (
        <div>
            <h1>Current Product</h1>
            {product ? (
                <>
                    <h2>Name: {product.name}</h2>
                    <p>ID: {product._id}</p>
                    <p>URL: {product.url}</p>
                    <p>Price: ${product.price_original}</p>
                    <p>Seller: {product.seller_name}</p>
                    {product.photos.map((photo, index) => (
                        <img key={index} src={photo} alt={`${photo} image`} />
                    ))}
                </>
            ) : (
                <p>No product found</p>
            )}
        </div>
    );
};

export default RandomProduct;
