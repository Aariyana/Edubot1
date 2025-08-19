from apscheduler.schedulers.asyncio import AsyncIOScheduler
from src.bot.utils.db import reset_daily_pdfs

async def on_startup():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(reset_daily_pdfs, "cron", hour=0, minute=0)  # daily reset
    scheduler.start()