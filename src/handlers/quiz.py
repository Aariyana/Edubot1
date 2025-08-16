from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.services.db import db

router = Router()

def register(dp):
    dp.include_router(router)

@router.message(Command("quiz"))
async def quiz(m: Message):
    q = db.quiz.aggregate([{ "$sample": {"size": 1}}]).next()
    opts = q.get("options", [])
    text = q.get("question") + "\n\n" + "\n".join([f"{i+1}. {o}" for i,o in enumerate(opts)])
    await m.answer(text + "\nReply with the option number.")
