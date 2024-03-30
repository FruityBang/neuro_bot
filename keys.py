from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Получить эмоджи')
        ],
        [
            KeyboardButton(text='Выбрать рубрику')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder='choice',
    selective=True
)