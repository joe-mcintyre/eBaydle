from pymongo import MongoClient
#import pymongo
from dotenv import load_dotenv
import json
import os

load_dotenv()

hostname = os.getenv('MONGO_HOST', 'localhost')  # Default to 'localhost' if not found
port = int(os.getenv('MONGO_PORT', 27017))       # Default to 27017 if not found

# Create a MongoClient instance
#client = MongoClient(host=hostname, port=port)
client = MongoClient(host=hostname, port=port)
"""
# Test the connection
try:
    client.admin.command('ping')
    print("MongoDB connection successful!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
"""


db = client.ebaydle
collection = db.product

def test_connection():
    try:
        client.ebaydle.command('ping')
        print("MongoDB connection successful!")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")

def db_add_product(json_data):
    try:
        if isinstance(json_data, list):
            # Insert multiple documents if the JSON file contains an array
            collection.insert_many(json_data)
            print("inserted many")
        else:
            # Insert a single document if the JSON file contains a single object
            collection.insert_one(json_data)
            print("inserted one")
        print("Data inserted successfully!")
        return 0
    except Exception as e:
        print(f"Error inserting data: {e}")
        return -1

def display_db():
    for collection_name in db.list_collection_names():
        print(f"Collection: {collection_name}")
        collection = db[collection_name]
        # displays all docs in all collections
        for document in collection.find():
            print(document)

def query_product_field(field_name, field_value):
    try:
        result = collection.find({f"{field_name}": f"{field_value}"})
        for product in result:
            print(product)
    except Exception as e:
        print(f"Error querying the collection: {e}")
