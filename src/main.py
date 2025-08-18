import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from src.handlers import start
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}
logging.basicConfig(level=logging.INFO)

async def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing! Please set it in Railway variables.")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Register routers
    dp.include_router(start.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped.")
