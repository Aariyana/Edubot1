from aiogram import types, Router
from aiogram.filters import Command
from src.bot.utils.db import get_user

router = Router()

@router.message(Command("profile", "me"))
async def user_profile(msg: types.Message):
    try:
        user = await get_user(msg.from_user.id)
        
        if not user:
            await msg.answer("❌ Profile not found. Please use /start first to create your account.")
            return
        
        # Get user data with default values
        name = user.get('name', msg.from_user.first_name)
        lang = user.get('lang', 'en')
        is_premium = user.get('is_premium', False)
        referrals = user.get('referrals', [])
        reward_points = user.get('reward_points', 0)
        daily_pdf_count = user.get('daily_pdf_count', 0)
        
        premium_status = "✅ Premium" if is_premium else "❌ Free"
        
        profile_text = f"""
        🏆 **Your Profile**

        👤 **Name:** {name}
        🌐 **Language:** {lang.upper()}
        💎 **Status:** {premium_status}
        📊 **Reward Points:** {reward_points}
        👥 **Referrals:** {len(referrals)} users
        📚 **Today's PDFs:** {daily_pdf_count}/3

        💡 **Tips:**
        • Use /pdf to search study materials
        • Use /referral to invite friends
        • Complete quizzes to earn points
        """
        
        await msg.answer(profile_text, parse_mode="Markdown")
        
    except Exception as e:
        print(f"Profile error: {e}")
        await msg.answer("⚠️ Temporary error loading profile. Please try again later.")