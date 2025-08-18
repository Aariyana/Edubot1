import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from fastapi import FastAPI
from src.handlers import start  # তোমাৰ bot handlers

logging.basicConfig(level=logging.INFO)

# FastAPI app (Railway uvicorn ত app launch হব)
app = FastAPI()

# Bot setup
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# Register routers
dp.include_router(start.router)


@app.on_event("startup")
async def on_startup():
    """Start bot polling when FastAPI starts"""
    asyncio.create_task(start_bot())


async def start_bot():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Bot polling crashed: {e}")


# Optional healthcheck endpoint
@app.get("/")
async def root():
    return {"status": "ok", "message": "Bot is running"}
