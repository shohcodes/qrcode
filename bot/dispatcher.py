import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from bot.utils import TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
bot.set_my_commands([BotCommand('start', 'Start using bot ✅'),
                     BotCommand('help', 'Support 👨‍💻')])
