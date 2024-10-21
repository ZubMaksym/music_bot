from .dispatcher_bot import dispatcher
from .bot import bot

async def main():
    await dispatcher.start_polling(bot)