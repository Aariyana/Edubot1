import aiohttp
from ..config import Config

async def post_to_blogger(blog_id: str, title: str, html_content: str):
    """Post to Blogger via API."""
    if not Config.BLOGGER_API_KEY:
        return {"error": "BLOGGER_API_KEY missing"}
    url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/?key={Config.BLOGGER_API_KEY}"
    payload = {"kind": "blogger#post", "title": title, "content": html_content}
    async with aiohttp.ClientSession() as s:
        async with s.post(url, json=payload) as r:
            return await r.json()