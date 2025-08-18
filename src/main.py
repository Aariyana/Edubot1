import os
import logging
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from src.handlers import start, profile  # Your handlers
from src.db import db  # MongoDB connection

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Initialize bot and dispatcher globally
bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Register handlers
dp.include_router(start.router)
dp.include_router(profile.router)

@app.get("/")
def health_check():
    return {"status": "active", "bot": "Edu Assam Bot"}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    try:
        update = await request.json()
        await dp.feed_update(bot, types.Update(**update))
        return {"status": "ok"}
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        return {"status": "error", "details": str(e)}

@app.on_event("startup")
async def on_startup():
    # Set webhook on startup
    webhook_url = f"https://{os.getenv('RENDER_EXTERNAL_HOSTNAME')}/webhook"
    await bot.set_webhook(webhook_url)
    logger.info(f"Webhook set to: {webhook_url}")

    # Optional: Clear pending updates
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Cleared pending updates")

if __name__ == "__main__":
    import uvicorn
    # Run FastAPI only (webhook mode doesn't need polling)
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))if __name__ == "__main__":
    import uvicorn
    import asyncio

    # FastAPI server (on PORT 8000)
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))

    # Run the bot (in background)
    asyncio.run(run_bot())
