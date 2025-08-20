import aiohttp
from ..config import Config

async def search_pdfs(query: str):
    """Return a list of PDF links using Google CSE."""
    if not (Config.GOOGLE_API_KEY and Config.CSE_ID):
        return []
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "cx": Config.CSE_ID,
        "key": Config.GOOGLE_API_KEY,
        "fileType": "pdf",
        "num": 5,
        "searchType": "search"
    }
    async with aiohttp.ClientSession() as s:
        async with s.get(url, params=params) as r:
            data = await r.json()
            items = data.get("items", []) if isinstance(data, dict) else []
            return [{"title": it["title"], "link": it["link"]} for it in items]

async def qa_answer(question: str):
    """Call your QA API and return text."""
    # TODO: Replace with your actual API
    return f"(demo) Answer for: {question}"

async def quiz_for(topic: str):
    """Call your Quiz API and return a simple list of Q/Options."""
    # TODO: Replace with your actual API
    return [
        {"q": f"{topic}: Demo Q1?", "options": ["A", "B", "C", "D"], "answer": "A"},
        {"q": f"{topic}: Demo Q2?", "options": ["True", "False"], "answer": "True"},
    ]