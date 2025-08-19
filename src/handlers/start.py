from aiogram import Router, types
from aiogram.filters import CommandStart
from db import db
from src.services.i18n import t
import secrets

router = Router()

@router.message(CommandStart())
async def on_start(message: types.Message):
    # ভাষা চিনাক্ত কৰা
    lang = (message.from_user.language_code or "en").split("-")[0]
    users = db.users
    
    # ব্যৱহাৰকাৰী ডাটাবেছত আছে নেকি চাওক
    user = users.find_one({"tg_id": message.from_user.id})
    
    if not user:
        # নতুন ব্যৱহাৰকাৰীৰ বাবে ডাটা সৃষ্টি কৰা
        referral_code = secrets.token_urlsafe(6)
        users.insert_one({
            "tg_id": message.from_user.id,
            "name": message.from_user.full_name,
            "lang": lang,
            "is_premium": False,
            "referral_code": referral_code,
            "reward_points": 0,
            "daily_pdf_count": 0
        })
    
    # স্বাগতম মেছেজ পঠিয়াওক
    await message.answer(
        t(lang, "start", name=message.from_user.first_name),
        parse_mode="Markdown"
    )
