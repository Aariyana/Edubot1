from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("quiz"))
async def on_quiz(msg: types.Message):
    await msg.answer("🧠 Daily Quiz Feature Coming Soon!")

@router.message(Command("question"))  
async def on_question(msg: types.Message):
    await msg.answer("❓ Question Answer Feature Coming Soon!")