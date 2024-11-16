import os
from aiogram.types import Message
from .dispatcher_bot import dispatcher
from .bot import bot
from .buttons import *
from aiogram.types import FSInputFile
from .keyboards_bot import *
from .texts_and_descriptions import *

@dispatcher.message()

async def handler(message: Message):
    chatID = message.chat.id

    voice_1_easy = FSInputFile(os.path.abspath(__file__ + f"../../../songs/easy_level/easy_audio_1.ogg"))
    voice_1_middle = FSInputFile(os.path.abspath(__file__ + f"../../../songs/middle_level/middle_audio_1.ogg"))
    voice_1_hard = FSInputFile(os.path.abspath(__file__ + f"../../../songs/hard_level/hard_audio_1.ogg"))

    if message.text == "Перейти до розспівок":
        await message.answer(text= "Чудово! Оберіть складність розспівки", reply_markup= main_keyboard)
    elif message.text == "Гайд на розспівки":
        await message.answer(text= guide_text)


    if message.text == "Початковий🎧":
        await bot.send_voice(chat_id=chatID, voice= voice_1_easy, protect_content= True, )
    elif message.text == "Середній🎶":
        await bot.send_voice(chat_id=chatID, voice= voice_1_middle, protect_content= True)
    elif message.text == "Складний💪":
        await bot.send_voice(chat_id=chatID, voice= voice_1_hard, protect_content= True)

    