from src.db import db

async def get_user(tg_id: int):
    try:
        return await db.users.find_one({"tg_id": tg_id})
    except:
        return None

async def get_top_users(limit=10):
    try:
        return await db.users.find().sort("reward_points", -1).limit(limit).to_list(limit)
    except:
        return []

async def count_users():
    try:
        return await db.users.count_documents({})
    except:
        return 0

async def get_all_users():
    try:
        return await db.users.find().to_list(None)
    except:
        return []

async def reset_daily_pdfs():
    try:
        await db.users.update_many({}, {"$set": {"daily_pdf_count": 0}})
    except:
        pass