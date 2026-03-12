import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TELEGRAM_BOT_TOKEN

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Приветствую Амиго 🤘\n\nЕсли ты хочешь поддержать меня, просто сосредоточься на себе.\n\nЕсли тебе хочется поиграть, кликни по кнопке GO в нижнем левом углу.')

@dp.message()
async def echo_handler(message: Message) -> None:
    await message.answer("Пиши только текст")

async def main() -> None:
    bot = Bot(token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())