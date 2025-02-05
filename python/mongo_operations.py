from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus
import json
import os

load_dotenv()

hostname = os.getenv('MONGO_HOST', 'localhost')  # 2nd parameter is default
port = int(os.getenv('MONGO_PORT', 27017))
username = os.getenv('MONGO_USERNAME')
password = os.getenv('MONGO_PASSWORD')
database_name = os.getenv('MONGO_DB')
db_collection = os.getenv('DB_COLLECTION')

if not username or not password:
    raise ValueError("username/password not set in .env")

# escape special characters
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# Create MongoClient instance with authentication
client = MongoClient(
    f"mongodb://{escaped_username}:{escaped_password}@{hostname}:{port}/{database_name}?authSource=admin"
)
db = client[database_name]
collection = db[db_collection]

# # Create MongoClient instance
# client = MongoClient(host=hostname, port=port)
# db = client.ebaydle
# collection = db.product

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
            print("Many Products Inserted")
        else:
            # Insert a single document if the JSON file contains a single object
            collection.insert_one(json_data)
            print("1 Product Inserted")
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
