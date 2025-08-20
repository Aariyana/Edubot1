from motor.motor_asyncio import AsyncIOMotorClient
from .config import Config

_client = AsyncIOMotorClient(Config.MONGO_URI)
_db = _client[Config.DB_NAME]

# Collections
users = _db["users"]
ads = _db["ads"]
referrals = _db["referrals"]
usage = _db["usage"]