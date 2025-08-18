# src/handlers/referral.py

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.db import db
from src.services.i18n import t

router = Router()

@router.message(Command("referral"))
async def on_referral(m: Message):
    lang = (m.from_user.language_code or "en").split("-")[0]
    users = db.users

    u = users.find_one({"tg_id": m.from_user.id})
    if not u:
        await m.answer(t(lang, "profile_not_found"))
        return

    referral_code = u.get("referral_code")
    invite_link = f"https://t.me/{(await m.bot.me()).username}?start={referral_code}"

    text = (
        f"🔗 {t(lang, 'your_referral_code')}: `{referral_code}`\n"
        f"👥 {t(lang, 'invite_friends')}: {invite_link}\n\n"
        f"🏆 {t(lang, 'reward_points')}: {u.get('reward_points', 0)}"
    )
    await m.answer(text, parse_mode="Markdown")
