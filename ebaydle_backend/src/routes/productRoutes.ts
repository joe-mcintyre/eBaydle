import express, { Request, Response } from "express";
import { ObjectId } from "mongodb";
import { collections } from "../services/database.service";
import Product from "../models/product";

//global config
export const router = express.Router();

router.use(express.json());

// maps collection to model //hopefully
const mapToProductModel = (dbRecord: any): Product => {
    return new Product(
        dbRecord.name,
        parseFloat(dbRecord.price_original.replace(/[^0-9.-]+/g, "")) || 0, // regex work pls
        dbRecord.url,
        dbRecord.photos || [],
        dbRecord.seller_name,
        dbRecord._id
    );
};

// GET ROUTE
router.get("/products", async (_req: Request, res: Response) => {
    try {
        if (!collections.products) {
            throw new Error("Products collection is not initialized.");
        }
        const dbRecords = await collections.products.find({}).toArray();
        const products = dbRecords.map(mapToProductModel);

        res.status(200).send(products);
    } catch (error) {
        const errorMessage = error instanceof Error ? error.message : "Unknown error occurred";
        res.status(500).send(errorMessage);
    }
});
