import os
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # required
    MONGO_URI = os.getenv("MONGO_URI")  # required
    DB_NAME = os.getenv("DB_NAME", "edubot")

    # Optional but recommended
    BLOGGER_API_KEY = os.getenv("BLOGGER_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    CSE_ID = os.getenv("CSE_ID")  # Custom Search Engine ID (for PDF search)
    ADMIN_IDS = {int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip().isdigit()}

    DEFAULT_BOT_PROPS = DefaultBotProperties(parse_mode=ParseMode.HTML)