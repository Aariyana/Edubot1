from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def fallback_handler(message: Message):
    await message.answer("🤖 I don't understand that command. Use /help for available commands.")