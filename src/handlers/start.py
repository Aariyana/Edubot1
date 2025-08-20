from aiogram import Router, types
from aiogram.filters import CommandStart
from src.db import db
import secrets

router = Router()

@router.message(CommandStart())
async def on_start(message: types.Message):
    user = await db.users.find_one({"tg_id": message.from_user.id})
    
    if not user:
        # New user - create profile
        await db.users.insert_one({
            "tg_id": message.from_user.id,
            "name": message.from_user.full_name,
            "lang": "en",
            "is_premium": False,
            "reward_points": 0,
            "daily_pdf_count": 0,
            "referrals": []
        })
    
    welcome_text = f"""
    👋 Hello {message.from_user.first_name}!
    
    I'm EduBot - Your Educational Assistant
    
    📚 Available Commands:
    /pdf - Find educational PDFs
    /quiz - Daily quizzes
    /profile - Your profile
    /referral - Invite friends, earn rewards
    
    Start with /pdf to find study materials!
    """
    
    await message.answer(welcome_text)
