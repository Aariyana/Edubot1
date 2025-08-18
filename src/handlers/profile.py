from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("profile"))
async def profile_command(message: types.Message):
    await message.answer("👤 Your profile info will be shown here.")
