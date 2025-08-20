from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from src.handlers import start, profile, referral, premium, quiz, pdf, help, admin, leaderboard, notifier, payment

async def set_commands(bot: Bot):
    await bot.set_my_commands([
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="pdf", description="Find & get PDFs"),
        BotCommand(command="referral", description="Referral link & rewards"),
        BotCommand(command="premium", description="Your premium status"),
        BotCommand(command="quiz", description="Daily quiz"),
        BotCommand(command="profile", description="Your profile"),
        BotCommand(command="help", description="Help information"),
        BotCommand(command="notify", description="Notify admin"),
        BotCommand(command="pay", description="Payment methods"),
    ])

def register(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(pdf.router)
    dp.include_router(referral.router)
    dp.include_router(premium.router)
    dp.include_router(quiz.router)
    dp.include_router(profile.router)
    dp.include_router(help.router)
    dp.include_router(admin.router)
    dp.include_router(leaderboard.router)
    dp.include_router(notifier.router)
    dp.include_router(payment.router)