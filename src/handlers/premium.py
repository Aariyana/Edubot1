# src/handlers/premium.py

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.db import db
from src.services.i18n import t

router = Router()

@router.message(Command("premium"))
async def on_premium(m: Message):
    lang = (m.from_user.language_code or "en").split("-")[0]
    users = db.users

    u = users.find_one({"tg_id": m.from_user.id})
    if not u:
        await m.answer(t(lang, "profile_not_found"))
        return

    if u.get("is_premium", False):
        await m.answer(t(lang, "already_premium"))
    else:
        await m.answer(
            t(lang, "not_premium") +
            "\n\n💳 To upgrade, please contact support or visit our premium page."
        )
