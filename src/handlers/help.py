from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from src.services.i18n import t

router = Router()

@router.message(Command("help"))
async def on_help(m: Message):
    lang = (m.from_user.language_code or "en").split("-")[0]
    await m.answer(t(lang, "help"))
