import os
import logging
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from src.handlers import start, profile  # তোমাৰ হেণ্ডলাৰসমূহ
from src.db import db  # MongoDB সংযোগ

# লগিং কনফিগাৰ কৰক
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "active", "bot": "Edu Assam Bot"}

async def run_bot():
    try:
        # বট ইনিচিয়েলাইজ কৰক
        bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)
        dp = Dispatcher()

        # হেণ্ডলাৰ ৰেজিষ্টাৰ কৰক
        dp.include_router(start.router)
        dp.include_router(profile.router)
        # অন্যান্য হেণ্ডলাৰ ইয়াত যোগ কৰিব পাৰে

        logger.info("বট চালু হৈছে...")
        await dp.start_polling(bot)

    except Exception as e:
        logger.error(f"ত্ৰুটি: {e}")
        raise

if __name__ == "__main__":
    import uvicorn
    import asyncio

    # FastAPI চাৰ্ভাৰ (PORT 8000 ত)
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))

    # বট চালু কৰক (Backgroundত)
    asyncio.run(run_bot())
