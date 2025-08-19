from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("refer"))
async def cmd_refer(message: types.Message):
    user_id = message.from_user.id
    ref_link = f"https://t.me/{message.bot.username}?start={user_id}"
    await message.answer(f"📨 Your referral link:\n{ref_link}\n\nInvite 10 friends = Get 4 hours free!")