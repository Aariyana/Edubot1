# src/bot.py - Simplified version
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

async def set_commands(bot: Bot):
    await bot.set_my_commands([
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="help", description="Show help"),
    ])

def register(dp: Dispatcher):
    # Create basic router here itself
    from aiogram import Router, types
    from aiogram.filters import Command
    
    router = Router()
    
    @router.message(Command("start"))
    async def start_handler(message: types.Message):
        await message.answer("🎓 Welcome to EduBot Assam!")
    
    @router.message(Command("help"))
    async def help_handler(message: types.Message):
        await message.answer("ℹ️ Help: Use /start to begin")
    
    dp.include_router(router)