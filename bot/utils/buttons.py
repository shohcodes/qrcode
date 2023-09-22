from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.utils import texts


async def colors_button():
    inline_button = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)
    inline_button.add(InlineKeyboardButton(texts.CLASSIC, callback_data='black'),
                      InlineKeyboardButton(texts.RED, callback_data='red'),
                      InlineKeyboardButton(texts.PURPLE, callback_data='purple'),
                      InlineKeyboardButton(texts.GREEN, callback_data='green'),
                      InlineKeyboardButton(texts.BROWN, callback_data='brown'),
                      InlineKeyboardButton(texts.YELLOW, callback_data='yellow'),
                      InlineKeyboardButton(texts.BLUE, callback_data='blue'))
    return inline_button
