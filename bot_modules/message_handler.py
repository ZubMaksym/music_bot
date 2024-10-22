from aiogram.types import Message
from .dispatcher_bot import dispatcher
from .bot import bot
from .buttons import eazy_level_button, middle_level_button, hard_level_button
import os
from aiogram.types import FSInputFile

@dispatcher.message()

async def handler(message: Message):
    chatID = message.chat.id

    voice_1_easy = FSInputFile(os.path.abspath(__file__ + f"../../../songs/easy_level/easy_audio_1.ogg"))
    voice_1_middle = FSInputFile(os.path.abspath(__file__ + f"../../../songs/middle_level/middle_audio_1.ogg"))
    voice_1_hard = FSInputFile(os.path.abspath(__file__ + f"../../../songs/hard_level/hard_audio_1.ogg"))

    if message.text == "Початковий🎧":
        await bot.send_voice(chat_id=chatID, voice= voice_1_easy, protect_content= True)
    elif message.text == "Середній🎶":
        await bot.send_voice(chat_id=chatID, voice= voice_1_middle, protect_content= True)
    elif message.text == "Складний💪":
        await bot.send_voice(chat_id=chatID, voice= voice_1_hard, protect_content= True)

    