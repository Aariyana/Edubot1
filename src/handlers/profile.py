from aiogram import types, Router
from aiogram.filters import Command

router = Router()

@router.message(Command("me"))
async def user_profile(msg: types.Message):
    try:
        user = await get_user(msg.from_user.id)
        if not user:
            await msg.answer("✗ User not found. Please /start again.")
            return

        premium_text = "Yes" if user.get('is_premium') else "No"
        
        text = f"""
        **Profile**
        Name: {user.get('name', msg.from_user.first_name)}
        Language: {user.get('lang', 'en')}
        Premium: {premium_text}
        Referrals: {len(user.get('referrals', []))}
        Reward Points: {user.get('reward_points', 0)}
        Daily PDFs: {user.get('daily_pdf_count', 0)}/3
        """
        await msg.answer(text, parse_mode="Markdown")
    
    except Exception as e:
        # Fallback if database has issues
        text = f"""
        **Profile**
        Name: {msg.from_user.first_name}
        Language: {msg.from_user.language_code or 'en'}
        Premium: No
        Referrals: 0
        Reward Points: 0
        Daily PDFs: 0/3
        
        ⚠️ Database temporarily unavailable
        """
        await msg.answer(text, parse_mode="Markdown")