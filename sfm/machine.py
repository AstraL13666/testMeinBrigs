import asyncio

import bot_text as b_txt
import user_text as u_txt

from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from configuration.config import bot
from data_quest.questions import all_data
from data_temporary.classes import Test, Answer
from keyboards.create import kbrd
from machine_calc.calculate import User
from sfm.question_generation import quest_gen, data


class UserTest(StatesGroup):
    mail = State()
    test = State()


async def get_mail(message: types.Message):
    Test.question = 1
    Answer.user = {}
    await message.answer(u_txt.start_test, reply_markup=ReplyKeyboardRemove())
    await UserTest.test.set()


async def testing(message: types.Message, state: FSMContext):
    # остановка теста
    if message.text.lower() == 'stop':
        Test.question = None
        Answer.user = {}

        await message.answer(b_txt.stop_test, parse_mode='HTML', reply_markup=ReplyKeyboardRemove())
        await state.finish()

    # сохранение вопроса
    elif message.text in all_data:
        Answer.user[Test.question] = message.text

        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await message.answer(b_txt.save_answer.format(Test.question, data[Test.question][0], message.text),
                             parse_mode='HTML')

        if Test.question == len(data.keys()):
            await message.answer('📝 Myers-Briggs, MBTI\n\nВы прошли тест!\n Ожидание результата через 2 секунды!')
            await asyncio.sleep(2)

            res = User(Answer.user).calculate()

            await message.answer(f'📝 Myers-Briggs, MBTI\n\n{res}', reply_markup=ReplyKeyboardRemove())

            Test.question = None
            Answer.user = {}

            await state.finish()

        else:
            if Test.question == 1:
                quest, a, b = quest_gen(True)
                await message.answer(quest, reply_markup=kbrd(a, b))
            else:
                quest, a, b = quest_gen(True)
                await message.answer(quest, reply_markup=kbrd(a, b))

    # введен левый текст
    else:
        if '@' in message.text.lower():
            await message.answer(text=b_txt.save_mail.format(message.text))
            quest, a, b = quest_gen(True)

        else:
            quest, a, b = quest_gen(False)
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await message.answer(text=b_txt.click_button, parse_mode='HTML')

        await message.answer(quest, reply_markup=kbrd(a, b))
