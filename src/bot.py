from aiogram import Bot, Dispatcher
from .config import Config

bot = Bot(token=Config.BOT_TOKEN, default=Config.DEFAULT_BOT_PROPS)
dp = Dispatcher()