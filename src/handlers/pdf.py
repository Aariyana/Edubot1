from aiogram import Router, types
from aiogram.filters import Command
from src.bot.utils.db import get_user
from src.services.cse import search_pdfs

router = Router()

@router.message(Command("pdf"))
async def on_pdf(msg: types.Message):
    user = await get_user(msg.from_user.id)
    
    if not user:
        await msg.answer("❌ Please use /start first to create your profile.")
        return
    
    # Check if user provided search query
    if len(msg.text.split()) < 2:
        await msg.answer("📚 **How to search PDFs:**\n\nExample: `/pdf class 10 maths algebra`\n\nExample: `/pdf NCERT science class 9`\n\nExample: `/pdf Assam board history`", parse_mode="Markdown")
        return
    
    search_query = msg.text.split(' ', 1)[1]
    await msg.answer(f"🔍 Searching for: _{search_query}_...", parse_mode="Markdown")
    
    try:
        # Search PDFs using your existing function
        results = search_pdfs(search_query)
        
        if not results:
            await msg.answer("❌ No PDFs found. Try a different search term or check your API keys.")
            return
        
        # Send results
        response = f"📚 **Found {len(results)} PDFs for** '_{search_query}_':\n\n"
        for i, result in enumerate(results, 1):
            title = result['title'][:50] + "..." if len(result['title']) > 50 else result['title']
            response += f"{i}. [{title}]({result['link']})\n   `{result['displayLink']}`\n\n"
        
        response += "\n💡 **Tip:** Use /question for any doubts about these materials!"
        await msg.answer(response, parse_mode="Markdown", disable_web_page_preview=True)
        
    except Exception as e:
        await msg.answer(f"❌ Search failed: {str(e)}")
        print(f"PDF search error: {e}")