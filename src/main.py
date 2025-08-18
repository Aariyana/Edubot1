import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from src.handlers import start  # অন্য handler থাকিলে তাতো include কৰিব পাৰা

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    # Register routers
    dp.include_router(start.router)

    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped.")
        
        from src.handlers import help, profile, referral

dp.include_router(help.router)
dp.include_router(profile.router)
dp.include_router(referral.router)
