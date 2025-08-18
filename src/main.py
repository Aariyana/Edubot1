import sys
from pathlib import Path
import os
import asyncio
from aiogram import Bot, Dispatcher
from fastapi import FastAPI

# Railway root fix
sys.path.append(str(Path(__file__).parent.parent))

from src.db import db
from src.handlers import start, help, profile, referral, premium, qa, pdf, quiz

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# include all routers
dp.include_router(start.router)
dp.include_router(help.router)
dp.include_router(profile.router)
dp.include_router(referral.router)
dp.include_router(premium.router)
dp.include_router(qa.router)
dp.include_router(pdf.router)
dp.include_router(quiz.router)

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    asyncio.create_task(dp.start_polling(bot))
