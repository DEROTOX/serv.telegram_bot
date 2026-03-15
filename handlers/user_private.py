from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Приветствую Амиго 🤘\n\nЕсли ты хочешь поддержать меня, просто сосредоточься на себе.\n\nЕсли тебе хочется поиграть, кликни по кнопке GO в нижнем левом углу.')

@user_private_router.message()
async def echo_handler(message: Message) -> None:
    await message.answer("Пиши только текст")