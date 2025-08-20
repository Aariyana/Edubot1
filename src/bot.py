from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from src.handlers import start, profile, pdf, referral, quiz, qa

async def set_commands(bot: Bot):
    await bot.set_my_commands([
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="pdf", description="Search educational PDFs"),
        BotCommand(command="question", description="Ask any question"),
        BotCommand(command="quiz", description="Daily quiz"),
        BotCommand(command="profile", description="Your profile"),
        BotCommand(command="referral", description="Referral program"),
    ])

def register(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(profile.router)
    dp.include_router(pdf.router)
    dp.include_router(qa.router)
    dp.include_router(quiz.router)
    dp.include_router(referral.router)