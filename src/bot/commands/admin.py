from aiogram import types, Router
from src.bot.utils.db import count_users, get_all_users
from aiogram.filters import Command
from aiogram.enums import ChatType

ADMIN_IDS = [123456789]  # তোমাৰ Telegram ID here
router = Router()

def is_admin(user_id: int):
    return user_id in ADMIN_IDS

@router.message(Command("stats"))
async def stats(msg: types.Message):
    if not is_admin(msg.from_user.id): return
    total = await count_users()
    await msg.answer(f"📊 Total Users: {total}")

@router.message(Command("broadcast"))
async def broadcast(msg: types.Message):
    if not is_admin(msg.from_user.id): return
    text = msg.text.split(" ", 1)[1]
    for u in await get_all_users():
        try:
            await msg.bot.send_message(u.tg_id, text)
        except: pass
    await msg.answer("✅ Broadcast done")
