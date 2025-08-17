from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.db import db

router = Router()

def register(dp):
    dp.include_router(router)

@router.message(Command("profile"))
async def profile(m: Message):
    u = db.users.find_one({"tg_id": m.from_user.id})
    if not u:
        return await m.answer("Start first: /start")
    txt = (
      f"Name: {u.get('name')}\n"
      f"Premium: {u.get('is_premium')}\n"
      f"Reward points: {u.get('reward_points')}\n"
      f"Daily PDF used: {u.get('daily_pdf_count',0)}/3\n"
      f"Referral link: t.me/YourBot?start={u.get('referral_code')}\n"
    )
    await m.answer(txt)
