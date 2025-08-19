import pymongo
from pymongo import Mongoclient

MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db = client["edu_bot"]
