import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile
from aiogram.utils import executor

from bot.dispatcher import dp
from bot.utils import buttons, texts
from bot.utils.service import create_qr_code, read_code_code


@dp.message_handler()
async def process_message(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = msg.text
    await msg.answer(texts.CHOOSE_COLOR, reply_markup=await buttons.colors_button())
    await state.set_state('color_set')


@dp.callback_query_handler(state='color_set')
async def else_(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['color'] = callback_query.data
    await create_qr_code(data)
    with open('qr_code.png', 'rb') as qr_file:
        await callback_query.message.answer_photo(photo=InputFile(qr_file),
                                                  caption=f"{data['title']}")
        await state.finish()
    os.remove('qr_code.png')
    await callback_query.message.delete()


@dp.message_handler(content_types=['photo'])
async def download_image(message: types.Message):
    await read_code_code(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
