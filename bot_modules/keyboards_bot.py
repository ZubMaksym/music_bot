import aiogram
from .inline_buttons import *

main_keyboard = aiogram.types.InlineKeyboardMarkup(
    inline_keyboard = [
        [eazy_level_button],
        [middle_level_button],
        [hard_level_button]
    ]
)