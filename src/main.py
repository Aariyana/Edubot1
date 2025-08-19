import os
import logging
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from src.handlers import start, profile
from src.db import db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "active", "bot": "Edu Assam Bot"}

# Aiogram bot runner
async def run_bot():
    try:
        bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)
        dp = Dispatcher()

        # include handlers
        dp.include_router(start.router)
        dp.include_router(profile.router)

        logger.info("Bot চালু হৈছে...")
        await dp.start_polling(bot)

    except Exception as e:
        logger.error(f"Bot error: {e}")
        raise

# FastAPI startup event → run bot in background
@app.on_event("startup")
async def startup_event():
    import asyncio
    asyncio.create_task(run_bot())
