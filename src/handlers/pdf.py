from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.db import db
from src.services.i18n import t

router = Router()

@router.message(Command("pdf"))
async def on_pdf(m: Message):
    lang = (m.from_user.language_code or "en").split("-")[0]
    users = db.users
    u = users.find_one({"tg_id": m.from_user.id})

    if not u:
        await m.answer(t(lang, "profile_not_found"))
        return

    if u.get("daily_pdf_count", 0) >= 3 and not u.get("is_premium", False):
        await m.answer(t(lang, "pdf_limit"))
        return

    users.update_one({"tg_id": m.from_user.id}, {"$inc": {"daily_pdf_count": 1}})
    await m.answer(t(lang, "pdf_generated"))
