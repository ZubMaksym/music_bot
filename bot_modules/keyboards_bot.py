import aiogram
from .buttons import *

main_keyboard = aiogram.types.ReplyKeyboardMarkup(
    keyboard = [
        [eazy_level_button],
        [middle_level_button],
        [hard_level_button]
    ]
)