import asyncio
import logging
import os
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp import web
from src.handlers import start  # নিশ্চিত কৰক যে এই import শুদ্ধ

# লগিং কনফিগাৰ কৰক
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI এপ্লিকেচন সৃষ্টি কৰক
app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

async def on_startup(bot: Bot):
    await bot.set_webhook("https://your-render-url.onrender.com/webhook")

async def main():
    # কনফিগাৰেচন লোড কৰক
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN এনভাইৰণমেন্ট ভেৰিয়েবল সেট কৰক!")
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # ৰাউটাৰ ৰেজিষ্টাৰ কৰক
    dp.include_router(start.router)
    
    # Webhook চেট আপ কৰক (ঐচ্ছিক)
    if os.getenv("WEBHOOK_MODE", "false").lower() == "true":
        await on_startup(bot)
        handler = SimpleRequestHandler(dp, bot=bot)
        handler.register(app, path="/webhook")
    else:
        # Polling মোড
        await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("বট বন্ধ কৰা হ'ল")
