from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from ..config import Config
from ..db import users
from datetime import datetime, timedelta

router = Router()

def is_admin(uid: int) -> bool:
    return uid in Config.ADMIN_IDS if Config.ADMIN_IDS else False

@router.message(Command("admin"))
async def admin_help(m: Message):
    if not is_admin(m.from_user.id):
        return
    await m.answer(
        "<b>Admin</b>\n"
        "/stats – total users\n"
        "/grant_premium <uid> <hours>\n"
    )

@router.message(Command("stats"))
async def stats(m: Message):
    if not is_admin(m.from_user.id):
        return
    total = await users.count_documents({})
    await m.answer(f"👥 Users: {total}")

@router.message(Command("grant_premium"))
async def grant(m: Message):
    if not is_admin(m.from_user.id):
        return
    parts = m.text.split()
    if len(parts) < 3:
        await m.answer("Usage: /grant_premium <uid> <hours>")
        return
    uid = int(parts[1]); hours = int(parts[2])
    until = datetime.utcnow() + timedelta(hours=hours)
    await users.update_one({"tg_id": uid}, {"$set": {"is_premium": True, "premium_until": until}}, upsert=True)
    await m.answer(f"✅ Premium granted to {uid} for {hours}h")