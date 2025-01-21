import { MongoClient, Db, Collection } from "mongodb";
import * as dotenv from "dotenv";

// Global Variables
export const collections: { products?: Collection } = {};

// Init Connection
export async function connectToDB(): Promise<void> {
  dotenv.config();

  // Ensure the connection string is defined
  const dbConnString = process.env.DB_CONN_STRING;
  if (!dbConnString) {
    throw new Error("DB_CONN_STRING environment variable not defined");
  }

  const client: MongoClient = new MongoClient(dbConnString);

  try {
    await client.connect();

    const db: Db = client.db(process.env.DB_NAME);

    const dbCollection = process.env.COLLECTION_NAME;
    if (!dbCollection) {
      throw new Error("COLLECTION_NAME environment variable not defined");
    }

    const productsCollection: Collection = db.collection(dbCollection);

    // Assign the collection to the global object
    collections.products = productsCollection;

    console.log(`CONNECTED TO DB: ${db.databaseName} & COLLECTION ${productsCollection.collectionName}`);
  } catch (error) {
    console.error("Error connecting to the database:", error);
    throw error;
  }
}
