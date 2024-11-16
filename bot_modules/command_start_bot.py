from aiogram.filters import CommandStart
from aiogram.types import Message
from .dispatcher_bot import dispatcher
from .keyboards_bot import *
from .texts_and_descriptions import say_hello_text

@dispatcher.message(CommandStart())

async def start_bot(message: Message):
    await message.answer(text= say_hello_text, reply_markup= choose_option_keyboard)

