from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from src.handlers import start, profile, pdf, referral, quiz

async def set_commands(bot: Bot):
    await bot.set_my_commands([
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="pdf", description="Find PDFs"),
        BotCommand(command="referral", description="Referral program"),
        BotCommand(command="quiz", description="Daily quiz"),
        BotCommand(command="profile", description="Your profile"),
    ])

def register(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(profile.router)
    dp.include_router(pdf.router)
    dp.include_router(referral.router)
    dp.include_router(quiz.router)

from src.handlers import fallback

def register(dp: Dispatcher):
    # ... other routers
    dp.include_router(fallback.router)  # শেষত add কৰক
