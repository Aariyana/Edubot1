from aiogram import types, Router
from datetime import datetime
from src.bot.utils.db import get_user

router = Router()

@router.message(commands=["me"])
async def user_profile(msg: types.Message):
    user = await get_user(msg.from_user.id)
    if not user:
        await msg.answer("❌ User not found. Please /start again.")
        return

    premium_text = "Yes (till {})".format(
        user.premium_until.strftime("%d-%m-%Y %H:%M")
    ) if user.is_premium else "No"

    text = f"""
👤 **Profile**
Name: {user.name or msg.from_user.first_name}
Language: {user.lang}
Premium: {premium_text}
Referrals: {len(user.referrals)}
Reward Points: {user.reward_points}
Daily PDFs: {user.daily_pdf_count}/3
"""
    await msg.answer(text, parse_mode="Markdown")
