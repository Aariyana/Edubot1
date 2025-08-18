import os
import logging
from fastapi import FastAPI
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from src.handlers import start, profile  # তোমাৰ হেণ্ডলাৰ

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "active", "bot": "Edu Assam Bot"}

async def run_bot():
    bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    
    # হেণ্ডলাৰ ৰেজিষ্টাৰ কৰক
    dp.include_router(start.router)
    dp.include_router(profile.router)
    
    logging.info("Polling মোডত বট চালু হৈছে...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    from hypercorn.asyncio import serve
    from hypercorn.config import Config
    
    # Hypercorn কনফিগাৰ কৰক (PORT 8000)
    config = Config()
    config.bind = ["0.0.0.0:8000"]
    
    # FastAPI আৰু Bot একেলগে চলাওক
    async def run():
        await asyncio.gather(
            serve(app, config),
            run_bot()
        )
    
    asyncio.run(run())
