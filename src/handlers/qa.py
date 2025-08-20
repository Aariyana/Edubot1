from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from ..services.google_search import qa_answer
from ..services.ads import is_ad_window_open

router = Router()

@router.message(Command("qa"))
async def qa_help(m: Message):
    await m.answer("❓ Use: <code>/qa your question</code>")

@router.message(F.text.startswith("/qa "))
async def qa_ask(m: Message):
    if not await is_ad_window_open(m.from_user.id):
        await m.answer("⏳ Please watch ads first: use /watch_ad then try again within 40s.")
        return
    q = m.text.split(" ", 1)[1].strip()
    ans = await qa_answer(q)
    await m.answer(f"<b>Answer:</b>\n{ans}")