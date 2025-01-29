import { useState } from "react";
import { getProductPrice } from './services/api';

function RevealPrice({ productID }: { productID: string }) {
    const [price, setPrice] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    async function fetchPrice() {
        setLoading(true);
        try {
            const { data } = await getProductPrice(productID);
            setPrice(data.price);
        } catch (error) {
            console.error("Error retrieving product price: ", error);
        } finally {
            setLoading(false);
        }
    }

    return (
        <div>
            <button onClick={fetchPrice} disabled={loading}>
                {loading ? "Loading..." : "GET PRICE"}
            </button>
            {price !== null && <div>{price}</div>}
        </div>
    );
}

export default RevealPrice;
