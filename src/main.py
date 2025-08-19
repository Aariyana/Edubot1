import os
import asyncio
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command

# ✅ Bot & Dispatcher
bot = Bot(
    token=os.getenv("BOT_TOKEN"),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# ✅ Simple handler
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("👋 Hello! EduBot is running successfully on Render.")

# ✅ FastAPI app with lifespan
async def lifespan(app: FastAPI):
    # Startup
    asyncio.create_task(dp.start_polling(bot))
    yield
    # Shutdown
    await bot.session.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"status": "EduBot is running 🚀"}
