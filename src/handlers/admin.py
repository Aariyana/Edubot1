from aiogram import types, Router
from aiogram.filters import Command
from src.bot.utils.db import count_users, get_all_users

ADMIN_IDS = [123456789]  # Replace with your Telegram ID
router = Router()

def is_admin(user_id: int):
    return user_id in ADMIN_IDS

@router.message(Command("stats"))
async def stats(msg: types.Message):
    if not is_admin(msg.from_user.id): 
        return
    total = await count_users()
    await msg.answer(f"All Total Users: {total}")

@router.message(Command("broadcast"))
async def broadcast(msg: types.Message):
    if not is_admin(msg.from_user.id): 
        return
    text = msg.text.split(" ", 1)[1]
    users = await get_all_users()
    for u in users:
        try:
            await msg.bot.send_message(u['tg_id'], text)
        except:
            pass
    await msg.answer("Broadcast done")