from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InputFile
from datetime import date
from src.db import db
from src.services.cse import search_pdfs
from src.services.i18n import t
import requests

router = Router()

def register(dp):
    dp.include_router(router)

@router.message(Command("pdf"))
async def pdf(m: Message):
    # Expected usage: /pdf class=6 subject=Maths lang=en
    args = m.text.split(maxsplit=1)
    query = args[1] if len(args) > 1 else "class 6 maths syllabus"

    u = db.users.find_one({"tg_id": m.from_user.id})
    if not u:
        return await m.answer("Start with /start")

    # Reset daily counter if date changed
    today = date.today().isoformat()
    if u.get("daily_pdf_date") != today:
        db.users.update_one({"tg_id": u["tg_id"]}, {"$set": {"daily_pdf_date": today, "daily_pdf_count": 0}})
        u = db.users.find_one({"tg_id": m.from_user.id})

    is_premium = u.get("is_premium", False)
    count = u.get("daily_pdf_count", 0)

    if not is_premium and count >= 3:
        return await m.answer("Daily limit reached (3). Get premium via referral or try tomorrow.")

    results = search_pdfs(query, num=5)
    if not results:
        return await m.answer("No PDFs found. Try a different query.")

    top = results[0]

    if is_premium:
        # Directly send file (stream as document by URL)
        await m.answer_document(document=top["link"], caption=top["title"])
    else:
        # Send Blogger gate URL (constructed) where 40s wait unlocks download
        gate_url = f"https://yourblog.blogspot.com/p/gate.html?u={top['link']}"
        await m.answer(f"Open to download after 40s: {gate_url}")
        db.users.update_one({"tg_id": u["tg_id"]}, {"$inc": {"daily_pdf_count": 1}})
