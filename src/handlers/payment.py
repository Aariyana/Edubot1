from aiogram import Router, types

router = Router()

@router.message(commands=["pay"])
async def cmd_pay(message: types.Message):
    await message.answer(
        "💰 Payment Method:\n\nSend UPI to: 7002561086@okbizaxis\n\nAfter payment, send screenshot to @abhijitedu"
    )
