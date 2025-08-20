from datetime import datetime, timedelta
from ..db import ads

AD_WINDOW_SECONDS = 40

async def grant_ad_window(user_id: int):
    until = datetime.utcnow() + timedelta(seconds=AD_WINDOW_SECONDS)
    await ads.update_one({"tg_id": user_id}, {"$set": {"allowed_until": until}}, upsert=True)

async def is_ad_window_open(user_id: int) -> bool:
    doc = await ads.find_one({"tg_id": user_id})
    return bool(doc and doc.get("allowed_until") and doc["allowed_until"] > datetime.utcnow())