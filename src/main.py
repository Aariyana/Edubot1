import os
import logging
import asyncio
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import start, profile, referral, notify, payment

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def home():
    return {"status": "active", "bot": "Edu Assam Bot", "help": "If you have any quarry send massage in @abhijitedu to help"}

async def run_bot():
    bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(profile.router)
    dp.include_router(referral.router)
    dp.include_router(notify.router)
    dp.include_router(payment.router)

    logger.info("🤖 Bot started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(run_bot())
