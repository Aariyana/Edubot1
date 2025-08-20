from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from datetime import datetime
from ..db import users

router = Router()

@router.message(Command("premium"))
async def premium_info(m: Message):
    u = await users.find_one({"tg_id": m.from_user.id}) or {}
    prem = u.get("is_premium", False)
    until = u.get("premium_until")
    if prem and until and until < datetime.utcnow():
        # expired
        await users.update_one({"tg_id": u["tg_id"]}, {"$set": {"is_premium": False}, "$unset": {"premium_until": 1}})
        prem = False
        until = None

    if prem:
        until_txt = until.strftime("%Y-%m-%d %H:%M:%S UTC") if until else "unknown"
        await m.answer(f"✅ Premium active.\nExpires: {until_txt}")
    else:
        await m.answer("❌ Premium not active.\nGet premium via referral: 10 referrals = 4 hours premium.")