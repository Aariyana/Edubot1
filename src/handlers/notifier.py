from aiogram import Router, types
from src.utils.notifier import send_admin_notify

router = Router()

@router.message(commands=["notify"])
async def cmd_notify(message: types.Message):
    await send_admin_notify(f"New notification from {message.from_user.id}: {message.text}")
    await message.answer("✅ Your message has been sent to admin.")
