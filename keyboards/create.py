from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def kbrd(text_a, text_b):
    but_a = KeyboardButton(text_a)
    but_b = KeyboardButton(text_b)
    but_stop = KeyboardButton('Stop')

    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(but_a).add(but_b).add(but_stop)


def general_menu():
    but_info = KeyboardButton('Информация')
    but_start_test = KeyboardButton('Начать тест')

    return ReplyKeyboardMarkup(resize_keyboard=True).row(but_start_test, but_info)
