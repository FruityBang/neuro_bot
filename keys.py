from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


rubrics_dict = {
    'Россия': 'russia/',
    'Мир': 'world/',
    'Бывший СССР': 'ussr/',
    'Экономика': 'economics/',
    'Силовые структуры': 'forces/',
    'Наука и техника': 'science/',
    'Культура': 'culture/',
    'Спорт': 'sport/',
    'Интернет и СМИ': 'media/',
    'Ценности': 'style/',
    'Путешествия': 'travel/',
    'Из жизни': 'life/',
    'Среда обитания': 'realty/',
    'Забота о себе': 'wellness/'
}


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Заказать случайную новость с главной')
        ],
        [
            KeyboardButton(text='Выбрать рубрику')
        ],
        [
            KeyboardButton(text='Псссс')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выбирай'
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Получить по заслугам', callback_data='kurwa')
        ]
    ]
)


def rubrics_keyboard():
    builder = ReplyKeyboardBuilder()
    [builder.button(text=rubric) for rubric in rubrics_dict]
    builder.button(text='НАЗАД')
    builder.adjust(3, 3, 3, 3, 3)
    return builder.as_markup(resize_keyboard=True)
