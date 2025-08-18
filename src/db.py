import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("MONGODB_DB", "edubot")]
#Define collections
users_col = db["users"]
referrals_col = db["referrals"]
premium_col = db["premium"]
quiz_col = db["quiz"]
