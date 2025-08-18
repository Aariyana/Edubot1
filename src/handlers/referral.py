from aiogram import Router, types
from aiogram.filters import Command
from src.db import users_col

router = Router()

@router.message(Command("referral"))
async def referral_command(message: types.Message):
    await message.answer("🔗 Here is your referral link!")
