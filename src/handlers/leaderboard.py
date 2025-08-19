from aiogram import Router, types
from aiogram.filters import Command
from src.bot.utils.db import get_top_users

router = Router()

@router.message(Command("rank"))
async def leaderboard(msg: types.Message):
    top_users = await get_top_users(limit=10)
    if not top_users:
        await msg.answer("No leaderboard data yet.")
        return

    text = "🏆 **Leaderboard**\n"
    for i, u in enumerate(top_users, 1):
        text += f"{i}. {u.get('name', 'User')} - {u.get('reward_points', 0)} pts\n"
    
    await msg.answer(text, parse_mode="Markdown")