import asyncio

from aiogram import Dispatcher, types
from configuration.config import bot

from sfm.machine import UserTest, get_mail, testing

from keyboards.create import general_menu
import user_text as txt



async def start(message: types.Message):
    await message.answer(txt.start, reply_markup=general_menu())


async def information(message: types.Message):
    await message.answer(txt.info, parse_mode='HTML')
    await asyncio.sleep(0.5)
    await message.answer('Выберите соответствующую кнопку!')


async def hole(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def reg_mes_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(information, text=['Информация'])
    dp.register_message_handler(get_mail, text='Начать тест')
    dp.register_message_handler(testing, state=UserTest.test)
    dp.register_message_handler(hole)
