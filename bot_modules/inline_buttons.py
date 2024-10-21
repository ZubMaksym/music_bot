import aiogram

eazy_level_button = aiogram.types.InlineKeyboardButton(text= "Початковий", callback_data= "beginner")
middle_level_button = aiogram.types.InlineKeyboardButton(text= "Середній", callback_data= "middle")
hard_level_button = aiogram.types.InlineKeyboardButton(text= "Складний", callback_data= "hard")

