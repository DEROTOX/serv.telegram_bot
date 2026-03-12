import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

TELEGRAM_BOT_TOKEN = os.getenv('BOT_TOKEN')