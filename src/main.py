import os
import logging
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from src.handlers import start, profile  # Your handlers
from src.db import db  # MongoDB connection

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "active", "bot": "Edu Assam Bot"}

async def run_bot():
    try:
        # Initialize bot
        bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)
        dp = Dispatcher()

        # Register handlers
        dp.include_router(start.router)
        dp.include_router(profile.router)
        # You can add other handlers here

        logger.info("Bot is starting...")
        await dp.start_polling(bot)

    except Exception as e:
        logger.error(f"Error: {e}")
        raise

if __name__ == "__main__":
    import uvicorn
    import asyncio

    # FastAPI server (on PORT 8000)
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))

    # Run the bot (in background)
    asyncio.run(run_bot())"

update with this
