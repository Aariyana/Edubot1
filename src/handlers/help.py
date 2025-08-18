from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("ℹ️ Available commands: /start, /profile, /referral, /premium, /qa, /pdf, /quiz")
