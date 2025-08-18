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

    referral_link = f"https://t.me/{(await m.bot.me()).username}?start={u['referral_code']}"
    await m.answer(t(lang, "referral", link=referral_link))
