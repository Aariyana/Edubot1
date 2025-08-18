import asyncio
import logging
import os
from aiogram import Bot, Dispatcher

# Import all handlers
from src.handlers import start, help, profile, referral, premium, qa, pdf, quiz

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    # Register routers (all handlers)
    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(profile.router)
    dp.include_router(referral.router)
    dp.include_router(premium.router)
    dp.include_router(qa.router)
    dp.include_router(pdf.router)
    dp.include_router(quiz.router)

    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped.")
