import os
import logging
import asyncio
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from src.handlers import start, profile
from src.db import db

# লগিং কনফিগাৰ কৰক
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "active", "bot": "Edu Assam Bot"}

# Bot চলোৱাৰ function
async def run_bot():
    from aiogram.client.default import DefaultBotProperties

bot = Bot(
    token=os.getenv("BOT_TOKEN"),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
    dp = Dispatcher()

    # হেণ্ডলাৰ ৰেজিষ্টাৰ কৰক
    dp.include_router(start.router)
    dp.include_router(profile.router)

    logger.info("🤖 Bot polling started...")
    await dp.start_polling(bot)

# Startup event → FastAPI server উঠিলেই bot খনো চলিব
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run_bot())   # backgroundত bot চলিব

if __name__ == "__main__":
    import uvicorn
    # একেই container ত FastAPI server চলিব
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
