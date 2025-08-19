import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.getenv("MONGODB_URI")  # Render uses MONGODB_URI
client = AsyncIOMotorClient(MONGO_URL)
db = client.edu_bot