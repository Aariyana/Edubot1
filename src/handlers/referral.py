from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("referral"))
async def cmd_referral(message: types.Message):
    referral_text = """
    📨 **Referral Program**
    
    Invite your friends and earn rewards!
    
    Your referral link: 
    `https://t.me/Edu_assam_bot?start=ref_(user_id)`
    
    🎁 Rewards:
    - 10 referrals = 4 hours premium
    - 50 referrals = 16 hours premium
    """
    
    await message.answer(referral_text, parse_mode="Markdown")