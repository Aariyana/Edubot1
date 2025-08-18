# src/handlers/profile.py

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.db import db
from src.services.i18n import t

router = Router()

@router.message(Command("profile"))
async def on_profile(m: Message):
    lang = (m.from_user.language_code or "en").split("-")[0]
    users = db.users
    u = users.find_one({"tg_id": m.from_user.id})

    if not u:
        await m.answer(t(lang, "profile_not_found"))
        return

    text = (
        f"👤 {u.get('name')}\n"
        f"🌐 Lang: {u.get('lang')}\n"
        f"⭐ Premium: {'Yes' if u.get('is_premium') else 'No'}\n"
        f"🏆 Points: {u.get('reward_points', 0)}\n"
        f"📄 Daily PDFs: {u.get('daily_pdf_count', 0)}"
    )
    await m.answer(text)
