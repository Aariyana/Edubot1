async def get_top_users(limit=10):
    return await db.users.find().sort("reward_points", -1).limit(limit).to_list(None)

async def count_users():
    return await db.users.count_documents({})

async def get_all_users():
    return await db.users.find().to_list(None)

async def reset_daily_pdfs():
    await db.users.update_many({}, {"$set": {"daily_pdf_count": 0}})
