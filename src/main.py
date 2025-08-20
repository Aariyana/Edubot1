import logging
import os
import asyncio

from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI
import uvicorn

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

# --- Bot command ---
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.reply("👋 Hello! Bot is running on Render Web Service.")

# --- FastAPI app (keep port open for Render) ---
app = FastAPI()

@app.get("/")
async def home():
    return {"status": "ok", "message": "Edu Bot is alive"}

async def start_bot():
    # Run polling in background
    asyncio.create_task(dp.start_polling())
    # Run FastAPI server to open port
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 10000)))

if __name__ == "__main__":
    asyncio.run(start_bot())