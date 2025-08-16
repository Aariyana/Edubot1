from aiogram import Router, types
from datetime import datetime
from src.db import users_col

router = Router()

@router.message(commands=["premium"])
async def premium_status(m: types.Message):
    u = users_col.find_one({"tg_id": m.from_user.id})
    if not u:
        return await m.answer("Use /start first.")
    until = u.get("premium_until")
    if u.get("is_premium") and until:
        left = max((until - datetime.utcnow()).total_seconds(), 0)
        hours = int(left // 3600)
        mins = int((left % 3600) // 60)
        return await m.answer(f"⭐ Premium active. Expires in {hours}h {mins}m.")
    await m.answer("You are not premium. Get premium via /referral (every 10 referrals = +3 hours).")
