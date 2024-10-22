from aiogram.filters import CommandStart
from aiogram.types import Message
from .dispatcher_bot import dispatcher
from .keyboards_bot import main_keyboard

@dispatcher.message(CommandStart())

async def start_bot(message: Message):
    await message.answer(
        text= 
    '''🎵Привіт!🎵\nЦе бот для розспівок. Обери складність розспівки:\n
            1)Початковий🎧: Прості вправи на дихання, артикуляцію, розігрів голосу. Підходять для тих, хто тільки починає займатися співом.\n
            2)Середній🎶: Вправи на розвиток діапазону, сили голосу, інтонації. Підходять для тих, хто має певний досвід співу.\n
            3)Професійний💪: Складні вправи, спрямовані на розвиток специфічних вокальних технік. Підходять для професійних співаків.''', 
reply_markup= main_keyboard)

