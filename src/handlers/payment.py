from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("pay"))
async def cmd_pay(message: types.Message):
    await message.answer(
        "💳 Payment Method:\n\n"
        "Send UPI to: 7002561086@okbizaxis\n\n"
        "After payment, send screenshot to @abhijitedu"
    )