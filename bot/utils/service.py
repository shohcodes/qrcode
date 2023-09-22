import os

import cv2
import qrcode
from aiogram import types
from pyzbar import pyzbar

from bot.dispatcher import bot
from bot.utils import texts


async def create_qr_code(data):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=100, border=4)
    qr.add_data(data['title'])
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color=f"{data['color']}", back_color="white")

    qr_image.save('qr_code.png')


async def read_code_code(message: types.Message):
    file_id = message.photo[-1].file_id
    photo_file = await bot.download_file_by_id(file_id)
    file_path = f"{file_id}.jpg"
    with open(file_path, 'wb') as f:
        f.write(photo_file.read())
    image = cv2.imread(f'{file_id}.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    if len(barcodes) > 0:
        qr_text = barcodes[0].data.decode('utf-8')
        await message.answer(qr_text)
    else:
        await message.answer(texts.NO_QR_CODE)
    os.remove(f'{file_id}.jpg')
