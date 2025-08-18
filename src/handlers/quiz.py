from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("quiz"))
async def quiz_command(message: types.Message):
    await message.answer("📝 Quiz feature is under development.")
