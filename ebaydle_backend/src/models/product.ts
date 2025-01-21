import { ObjectTd } from "mongodb";

// Class Implementation
export default class Product {
    constructor(public name: string, public price: number,
               public page_url: string, public images: string[],
               public id?: ObjectId)
}
