from aiogram import types
from bot.dispatcher import dp
from db.config import DB


@dp.message_handler(commands='help')
async def help_handler(msg: types.Message):
    await msg.answer("If you need help,please contact us ✅\nContact📞: @shohcodes")


@dp.message_handler(commands='start')
async def start_handler(msg: types.Message):
    await msg.answer(f'Salom {msg.from_user.first_name.title()} 😊')
    await msg.answer("Istalgan matn kiriting yoki QR kod yuboring: 👇")
    check_user = DB().select_user(str(msg.from_user.id))
    if check_user is None:
        DB().insert_into(user_id=str(msg.from_user.id), username=msg.from_user.username,
                         full_name=msg.from_user.full_name)
