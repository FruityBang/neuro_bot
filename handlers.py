from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReactionTypeEmoji, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.enums.dice_emoji import DiceEmoji
import keys
from random import choice
import parser
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest


dp = Dispatcher()
random_rubric = None
test_list = [
    ['1', '2', '/articles/2024/04/02/catastrophe/'],
    ['3', '4', '/news/2024/04/03/v-rossii-podrostok-zadal-sverstniku-vopros-i-izbil-ego-pod-video/'],
    ['5', 'курва', '/news/2024/04/03/v-rossii-podrostok-zadal-sverstniku-vopros-i-izbil-ego-pod-video/'],
    ['6', 'курва3', '/news/2024/04/03/v-rossii-podrostok-zadal-sverstniku-vopros-i-izbil-ego-pod-video/']
]


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


@dp.message(F.text.lower() == 'псссс')
async def get_kurwa(message: Message):
    lottery = await message.answer_dice(DiceEmoji.SLOT_MACHINE)
    global random_rubric
    random_rubric = lottery.dice.value
    await message.answer(
        'Sector kurwa is on the drum',
        reply_markup=keys.inline_keyboard
    )


@dp.message(F.text.lower().startswith('заказать'))
async def get_kurwa(message: Message):

    await message.answer(
        'Заказать'
    )


@dp.message(F.text.lower().startswith('выбрать'))
async def get_rubric(message: Message):
    await message.answer(
        'выбирай',
        reply_markup=keys.rubrics_keyboard()
    )


@dp.callback_query(F.data.lower() == 'kurwa')
async def get_kurwa2(callback: CallbackQuery):
    print(random_rubric)
    await callback.message.answer('KKK')


@dp.message(F.photo)
async def get_photo(message: Message):
    print(F.photo)
    await message.answer('Ok kurwa. I got photo')
    print(message.photo)
    # print(bot.get_file(message.photo))


@dp.message(F.text.in_(keys.rubrics_dict))
async def rubric_chosen(message: Message):

    if message.text in keys.rubrics_dict:
        news_list = parser.get_rubric_news(suff=keys.rubrics_dict[message.text])
        exist_session = keys.UserNews.get(message.from_user.id)

        if not exist_session:
            keys.UserNews(user=message.from_user.id, news_list=news_list)

        else:
            exist_session[0].news_list = news_list

        await message.answer(
            f'{news_list[0][0]} - {news_list[0][1]}',
            reply_markup=keys.paginator()
        )


@dp.callback_query(keys.NewsPagination.filter(F.action.in_(['prev', 'next'])))
async def news_pagination(callback: CallbackQuery, callback_data: keys.NewsPagination):
    page_num = int(callback_data.page)
    news_list = keys.UserNews.get(callback.from_user.id)[0].news_list
    if callback_data.action == 'prev':
        print('prev')
        page = page_num - 1 if page_num > 0 else 0
    if callback_data.action == 'next':
        print('next')
        page = page_num + 1 if page_num < (len(news_list) - 1) else page_num
    with suppress(TelegramBadRequest):
        await callback.message.edit_text(
            f'{news_list[page][0]} - {news_list[page][1]}',
            reply_markup=keys.paginator(page=page)
        )
    await callback.answer()


@dp.message()
async def echo(message: Message):
    await message.answer(message.text)
    await message.answer('<b>type /start command</b>')


@dp.callback_query()
async def echo_callback(callback: CallbackQuery):

    await callback.message.answer(callback.data)
    await callback.message.answer('lll')
