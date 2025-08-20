from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from ..db import users

router = Router()

@router.message(Command("profile"))
async def profile(m: Message):
    u = await users.find_one({"tg_id": m.from_user.id}) or {}
    is_premium = "✅" if u.get("is_premium") else "❌"
    await m.answer(
        "<b>Your Profile</b>\n"
        f"Name: {u.get('name', m.from_user.full_name)}\n"
        f"Premium: {is_premium}\n"
        f"Points: {u.get('points', 0)}"
    )