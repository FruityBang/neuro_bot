from aiogram import Bot, Dispatcher, F
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.types import Message, ReactionTypeEmoji, CallbackQuery
from contextlib import suppress
from random import choice

import keys
import main
import parser


dp = Dispatcher()


@dp.message(CommandStart())
async def get_start(message: Message, bot: Bot):
    emos = ['👍', '❤', '🔥', '😍', '💋']
    reaction = ReactionTypeEmoji(emoji=choice(emos))
    await message.react([reaction])
    await bot.send_message(
        message.from_user.id,
        f'Lets get started, mr {message.from_user.first_name} kurwa',
        reply_markup=keys.main_keyboard
    )


@dp.message(F.text.lower().startswith('выбрать'))
async def get_rubric(message: Message):
    await message.answer(
        'выбирай',
        reply_markup=keys.rubrics_keyboard()
    )


@dp.message(F.text.lower() == 'псссс')
async def get_kurwa(message: Message):
    await message.answer(
        'Sector kurwa is on the drum',
        reply_markup=keys.secret_inline_keyboard
    )


@dp.callback_query(F.data.lower() == 'kurwa')
async def get_wisdom(callback: CallbackQuery):
    await callback.message.answer_dice(DiceEmoji.SLOT_MACHINE)
    secret_wisdom = await parser.get_po_zaslugam()
    await callback.message.answer(secret_wisdom, reply_markup=keys.main_keyboard)
    await main.bot.delete_message(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id
    )


@dp.message(F.text == 'НАЗАД')
async def get_back(message: Message):
    await message.answer(
        text='По новой',
        reply_markup=keys.main_keyboard
    )


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer('Ok. I got photo')


@dp.message(F.text.in_(keys.rubrics_dict))
async def rubric_chosen(message: Message):

    if message.text in keys.rubrics_dict:
        news_list = await parser.get_rubric_news(suff=keys.rubrics_dict[message.text])
        exist_session = keys.UserNews.get(message.from_user.id)

        if not exist_session:
            keys.UserNews(user=message.from_user.id, news_list=news_list)

        else:
            exist_session[0].news_list = news_list

        await message.answer(
            f'<b>!ПЕРЕДОВИЦА!\n</b><i>- {news_list[0][0]} -</i>\n{news_list[0][1]}',
            reply_markup=keys.paginator()
        )


@dp.callback_query(keys.NewsPagination.filter(F.action.in_(['prev', 'next'])))
async def news_pagination(callback: CallbackQuery, callback_data: keys.NewsPagination):
    page_num = int(callback_data.page)
    news_list = keys.UserNews.get(callback.from_user.id)[0].news_list
    if callback_data.action == 'prev':
        page = page_num - 1 if page_num > 0 else 0
    else:
        page = page_num + 1 if page_num < (len(news_list) - 1) else page_num
    with suppress(TelegramBadRequest):
        await callback.message.edit_text(
            f'<i>- {news_list[page][0]} -</i>\n{news_list[page][1]}',
            reply_markup=keys.paginator(page=page)
        )
    await callback.answer()


@dp.callback_query(keys.NewsPagination.filter(F.action == 'read'))
async def read_new(callback: CallbackQuery, callback_data: keys.NewsPagination):
    page = int(callback_data.page)
    url = keys.UserNews.get(callback.from_user.id)[0].news_list[page][2]
    if not page:
        await callback.message.answer(
            'Заглавный материал доступен на сайте',
            reply_markup=keys.button_for_main(parser.news_link+url)
        )
    else:
        photo, new_to_display = await parser.get_new(suff=url)
        await callback.message.answer_photo(photo)
        await callback.message.answer(new_to_display)


@dp.message(F.text.lower().startswith('заказать'))
async def get_random(message: Message):
    news_list = await parser.get_rubric_news(suff=keys.rubrics_dict[choice(list(keys.rubrics_dict))])
    url = choice(news_list[1:])[2]
    photo, new_to_display = await parser.get_new(suff=url)
    await message.answer_photo(photo)
    await message.answer(new_to_display)


@dp.message()
async def echo(message: Message):
    await message.answer('<b>type /start command</b>')


@dp.callback_query()
async def echo_callback(callback: CallbackQuery):
    await callback.message.answer(callback.data)
