import mongoose, { Schema, Document } from 'mongoose';

export interface Product extends Document {
    name: string;
    price: number;
}

const productSchema = new Schema<Product>({
    name: { type: String, required: true },
    price: { type: Number, required: true },
});

const Product = mongoose.model<Product>('Product', productSchema);
export default Product;
