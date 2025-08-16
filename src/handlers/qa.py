from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.services.cse import search_pdfs
from src.services.notes import summarize_pdf_url

router = Router()

def register(dp):
    dp.include_router(router)

@router.message(Command("question"))
async def question(m: Message):
    # /question class=10 subject=Science chapter=Acids
    query = m.text.split(maxsplit=1)
    q = query[1] if len(query) > 1 else "class 10 science important questions"
    results = search_pdfs(q, num=3)
    if not results:
        return await m.answer("No results found.")
    # Make a tiny extractive summary from first PDF to show as short notes
    try:
        short = summarize_pdf_url(results[0]["link"], sentences=4)
    except Exception:
        short = "Short notes unavailable for this file."
    await m.answer(short[:3500])  # Telegram message limit safety
