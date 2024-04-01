from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReactionTypeEmoji, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.enums.dice_emoji import DiceEmoji
from keys import main_keyboard, inline_keyboard, rubrics_keyboard
from random import choice


dp = Dispatcher()
random_rubric = None


@dp.message(CommandStart())
async def get_start(message: Message, bot: Bot):
    emos = ['👍', '❤', '🔥', '😍', '💋']
    reaction = ReactionTypeEmoji(emoji=choice(emos))
    await message.react([reaction])
    await bot.send_message(
        message.from_user.id,
        f'Lets get started, mr {message.from_user.first_name} kurwa',
        reply_markup=main_keyboard
    )


@dp.message(F.text.lower() == 'псссс')
async def get_kurwa(message: Message):
    lottery = await message.answer_dice(DiceEmoji.SLOT_MACHINE)
    global random_rubric
    random_rubric = lottery.dice.value
    await message.answer(
        'Sector kurwa is on the drum',
        reply_markup=inline_keyboard
    )


@dp.message(F.text.lower().startswith('заказать'))
async def get_kurwa(message: Message):
    await message.answer(
        'Заказать'
    )


@dp.message(F.text.lower().startswith('выбрать'))
async def get_kurwa(message: Message):
    await message.answer(
        'выбрай',
        reply_markup=rubrics_keyboard()
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


@dp.message()
async def echo(message: Message):
    print(message)
    await message.answer('type /start command')
