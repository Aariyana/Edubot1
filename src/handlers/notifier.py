from aiogram import Router, types
from aiogram.filters import Command
from src.utils.notifier import send_admin_notify

router = Router()

@router.message(Command("notify"))
async def cmd_notify(message: types.Message):
    # Fixed f-string formatting
    notification_text = f"New notification from {message.from_user.id}: {message.text}"
    await send_admin_notify(notification_text)
    await message.answer("✅ Your message has been sent to admin.")