from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from src.db import db
from src.services.i18n import t
import secrets

router = Router()

@router.message(CommandStart())
async def on_start(m: Message):
    lang = (m.from_user.language_code or "en").split("-")[0]
    users = db.users
    u = users.find_one({"tg_id": m.from_user.id})

    if not u:
        referral_code = secrets.token_urlsafe(6)
        users.insert_one({
            "tg_id": m.from_user.id,
            "name": m.from_user.full_name,
            "lang": lang,
            "is_premium": False,
            "referral_code": referral_code,
            "reward_points": 0,
            "daily_pdf_count": 0,
        })

    await m.answer(t(lang, "start", name=m.from_user.first_name))
