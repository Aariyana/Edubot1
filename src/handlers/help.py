from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def help_handler(message: types.Message):
    help_text = """
    📚 Available Commands:
    /start - Start the bot
    /help - Show this help
    /pdf - Find PDFs
    /profile - Your profile
    """
    await message.answer(help_text)