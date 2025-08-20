from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from ..services.google_search import search_pdfs
from ..services.ads import is_ad_window_open

router = Router()

@router.message(Command("pdf"))
async def pdf_help(m: Message):
    await m.answer("🔎 Use: <code>/pdf your topic</code>")

@router.message(F.text.startswith("/pdf "))
async def pdf_search(m: Message):
    # ad gate (unless premium, but for demo we just check ad window)
    if not await is_ad_window_open(m.from_user.id):
        await m.answer("⏳ Please watch ads first: use /watch_ad then try again within 40s.")
        return
    query = m.text.split(" ", 1)[1].strip()
    results = await search_pdfs(query)
    if not results:
        await m.answer("No PDF found or API not configured.")
        return
    text = "📄 <b>PDF Results</b>\n" + "\n".join([f"• <a href='{x['link']}'>{x['title']}</a>" for x in results])
    await m.answer(text)