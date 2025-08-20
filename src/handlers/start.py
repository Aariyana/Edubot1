from aiogram import Router, types
from aiogram.filters import CommandStart
from src.db import db
import secrets

router = Router()

@router.message(CommandStart())
async def on_start(message: types.Message):
    try:
        user = await db.users.find_one({"tg_id": message.from_user.id})
        
        if not user:
            # Create new user
            user_data = {
                "tg_id": message.from_user.id,
                "name": message.from_user.full_name,
                "lang": "en",
                "is_premium": False,
                "reward_points": 100,  # Starting bonus
                "daily_pdf_count": 0,
                "referrals": [],
                "created_at": message.date
            }
            
            result = await db.users.insert_one(user_data)
            if result.inserted_id:
                print(f"New user created: {message.from_user.id}")
        
        welcome_text = f"""
        🎓 **Welcome to EduBot, {message.from_user.first_name}!**

        📚 **I'm your educational assistant for:**
        • NCERT & CBSE Materials
        • Assam Board Syllabus  
        • PDF Study Resources
        • Quiz & Learning

        🚀 **Get Started:**
        /pdf - Search educational PDFs
        /question - Ask any doubt
        /quiz - Test your knowledge
        /profile - View your progress
        /referral - Invite friends, earn rewards

        💡 **Tip:** Start with `/pdf class 10 maths` to find materials!
        """
        
        await message.answer(welcome_text, parse_mode="Markdown")
        
    except Exception as e:
        print(f"Start error: {e}")
        await message.answer("👋 Welcome! Use /help to see available commands.")