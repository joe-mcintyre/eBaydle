import { ObjectId } from "mongodb";

// Class Implementation
export default class Product {
    constructor(public name: string, public price_original: number,
               public url: string, public photos: string[],
               public seller_name: string, public _id?: ObjectId) {}
}
