import os
import logging
import asyncio
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from src.bot import register, set_commands

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def home():
    return {"status": "active", "bot": "Edu Assam Bot"}

async def run_bot():
    # Fixed: Use DefaultBotProperties instead of parse_mode parameter
    bot = Bot(
        token=os.getenv("BOT_TOKEN"), 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    # Register handlers and setup
    register(dp)
    await set_commands(bot)
    
    logger.info("🤖 Bot started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(run_bot())