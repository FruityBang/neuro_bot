from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


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
            KeyboardButton(text='Заказать случайную новость')
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

secret_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Получить по заслугам', callback_data='kurwa')
        ],
    ]
)


def rubrics_keyboard():
    builder = ReplyKeyboardBuilder()
    [builder.button(text=rubric) for rubric in rubrics_dict]
    builder.button(text='НАЗАД')
    builder.adjust(3, 3, 3, 3, 3)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


class UserNews:
    instances = []

    def __init__(self, user, news_list):
        self.user = user
        self.news_list = news_list
        UserNews.instances.append(self)

    @classmethod
    def get(cls, value):
        return [inst for inst in cls.instances if inst.user == value]


class NewsPagination(CallbackData, prefix='pagination'):
    action: str
    page: int


def paginator(page: int = 0):
    builder = InlineKeyboardBuilder()
    print(f'page {page}')
    builder.row(
        InlineKeyboardButton(
            text='⬅', callback_data=NewsPagination(action='prev', page=page).pack()
        ),
        InlineKeyboardButton(
            text='читать полностью', callback_data=NewsPagination(action='read', page=page).pack()
        ),
        InlineKeyboardButton(
            text='➡', callback_data=NewsPagination(action='next', page=page).pack()
        ),
        width=1
    )
    return builder.as_markup()

def button_for_main(url: str):
    inline_keyboard_for_main = InlineKeyboardBuilder()
    inline_keyboard_for_main.button(text='перейти', url=url)
    return inline_keyboard_for_main.as_markup()

