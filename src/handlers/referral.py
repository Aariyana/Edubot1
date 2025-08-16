from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime, timedelta
from src.services.db import db

router = Router()

def register(dp):
    dp.include_router(router)

@router.message(Command("referral"))
async def referral(m: Message):
    u = db.users.find_one({"tg_id": m.from_user.id})
    if not u:
        return await m.answer("Use /start first")
    await m.answer(
      "Share your link: t.me/YourBot?start=" + u.get("referral_code", "") +
      "\nEach successful join gives 1 day premium."
    )
