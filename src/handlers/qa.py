from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.services.i18n import t

router = Router()

@router.message(Command("qa"))
async def on_qa(m: Message):
    lang = (m.from_user.language_code or "en").split("-")[0]
    await m.answer(t(lang, "qa_info"))
