from aiogram.types import CallbackQuery
from .dispatcher_bot import dispatcher


@dispatcher.callback_query()

async def callback_handler(callback: CallbackQuery):
    if callback.data == "beginner":
        await callback.answer(text= "🎧Ви обрали рівнеь початківця🎧")
    elif callback.data == "middle":
        await callback.answer(text= "🎶Ви обрали середній рівень🎶")
    elif callback.data == "hard":
        await callback.answer(text= "💪Ви обрали складний рівень💪")