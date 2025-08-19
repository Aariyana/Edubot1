from aiogram import Bot
import os

bot = Bot(token=os.getenv("BOT_TOKEN"))

async def send_admin_notify(message: str):
    admin_id = os.getenv("ADMIN_ID")
    if admin_id:
        await bot.send_message(chat_id=admin_id, text=message)
