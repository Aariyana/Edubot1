from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from ..db import users
from datetime import datetime

router = Router()

@router.message(CommandStart())
async def on_start(m: Message):
    uid = m.from_user.id
    lang = (m.from_user.language_code or "en").split("-")[0]
    u = await users.find_one({"tg_id": uid})
    if not u:
        await users.insert_one({
            "tg_id": uid,
            "name": m.from_user.full_name,
            "lang": lang,
            "joined_at": datetime.utcnow(),
            "is_premium": False,
            "ref_code": None,
            "points": 0
        })
    await m.answer(
        "👋 <b>Welcome!</b>\n"
        "আমি Edu Assam Bot.\n"
        "• /profile – তোমাৰ তথ্য\n"
        "• /pdf – PDF সন্ধান/ডাউনলোড\n"
        "• /qa – প্রশ্নোত্তৰ\n"
        "• /quiz – কুইজ\n"
        "• /premium – প্ৰিমিয়াম তথ্য\n"
        "• /referral – ৰেফাৰেল সুবিধা\n"
        "\nIf you have any query, send a message to <a href='https://t.me/abhijitedu'>@abhijitedu</a> to help."
    )