from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from src.handlers import pdf as pdf_handler
from src.handlers import referral as ref_handler
from src.handlers import premium as prem_handler
from src.handlers import quiz as quiz_handler   # if added
from src.handlers import profile as profile_handler

async def set_cmds(bot: Bot):
    await bot.set_my_commands([
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="pdf", description="Find & get PDFs"),
        BotCommand(command="referral", description="Referral link & rewards"),
        BotCommand(command="premium", description="Your premium status"),
        BotCommand(command="quiz", description="Daily quiz"),
        BotCommand(command="profile", description="Your profile"),
    ])

def register(dp: Dispatcher):
    dp.include_router(pdf_handler.router)
    dp.include_router(ref_handler.router)
    dp.include_router(prem_handler.router)
    dp.include_router(quiz_handler.router)
    dp.include_router(profile_handler.router)
