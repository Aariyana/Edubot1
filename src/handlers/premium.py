from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("premium"))
async def premium_command(message: types.Message):
    await message.answer("💎 Premium features coming soon!")
