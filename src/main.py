
import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from fastapi import FastAPI, Request
from src.services.db import db
from src.handlers import start, help, profile, referral, premium, qa, pdf, quiz

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# Register handlers
start.register(dp)
help.register(dp)
profile.register(dp)
referral.register(dp)
premium.register(dp)
qa.register(dp)
pdf.register(dp)
quiz.register(dp)

app = FastAPI()

@app.get("/")
async def health():
    return {"ok": True}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    await dp.feed_webhook_update(bot=bot, update=update)
    return {"ok": True}

async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)

if __name__ == "__main__":
    import uvicorn
    asyncio.get_event_loop().run_until_complete(on_startup())
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
