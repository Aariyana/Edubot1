from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("pdf"))
async def pdf_command(message: types.Message):
    await message.answer("📄 Send me a file and I'll process it.")
