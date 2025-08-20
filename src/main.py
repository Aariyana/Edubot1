import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

# Bot init
BOT_TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

# Dispatcher init (no bot here)
dp = Dispatcher()


# Handlers
@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("👋 Hello! I am your Edu Bot. If you have any query send message at @abhijitedu")


@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer("ℹ️ Use /start to begin.\nIf you face issues, contact admin @abhijitedu.")


# Run
async def main():
    logging.info("🤖 Bot starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())