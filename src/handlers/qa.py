from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("qa"))
async def qa_command(message: types.Message):
    await message.answer("❓ Ask your question...")
