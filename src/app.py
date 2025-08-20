import asyncio
import logging
from fastapi import FastAPI
from .bot import bot, dp
from .handlers import start, profile, referral, premium, pdf, qa, quiz, admin

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Edu Assam Bot")

# include routers
dp.include_router(start.router)
dp.include_router(profile.router)
dp.include_router(referral.router)
dp.include_router(premium.router)
dp.include_router(pdf.router)
dp.include_router(qa.router)
dp.include_router(quiz.router)
dp.include_router(admin.router)

@app.get("/")
def health():
    return {"ok": True, "service": "Edu Assam Bot"}

# Background polling
_polling_task: asyncio.Task | None = None

@app.on_event("startup")
async def on_startup():
    global _polling_task
    logger.info("Starting Telegram polling as background task...")
    _polling_task = asyncio.create_task(dp.start_polling(bot))

@app.on_event("shutdown")
async def on_shutdown():
    logger.info("Shutting down bot...")
    if _polling_task:
        _polling_task.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await _polling_task
    await bot.session.close()

# Needed import
import contextlib