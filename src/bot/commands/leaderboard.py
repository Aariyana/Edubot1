from aiogram import types, Router
from src.bot.utils.db import get_top_users

router = Router()

@router.message(commands=["rank"])
async def leaderboard(msg: types.Message):
    top_users = await get_top_users(limit=10)
    if not top_users:
        await msg.answer("No leaderboard data yet.")
        return

    text = "🏆 **Leaderboard**\n"
    for i, u in enumerate(top_users, 1):
        text += f"{i}. {u.name or 'User'} – {u.reward_points} pts\n"

    await msg.answer(text, parse_mode="Markdown")
