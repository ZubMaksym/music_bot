from aiogram.filters import CommandStart
from aiogram.types import Message
from .dispatcher_bot import dispatcher
from .keyboards_bot import main_keyboard

@dispatcher.message(CommandStart())

async def start_bot(message: Message):
    await message.answer(text= "🎵Привіт!🎵\nЦе бот для розспівок. Обери складність розспівки", reply_markup= main_keyboard)

