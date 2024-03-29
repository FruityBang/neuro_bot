from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReactionTypeEmoji
from aiogram.filters import Command, CommandStart
from aiogram.enums.dice_emoji import DiceEmoji
from keys import main_keyboard
from random import choice


dp = Dispatcher()



@dp.message(CommandStart())
async def get_start(message: Message, bot: Bot):
    emos = ['👍', '❤', '🔥', '😍', '💋']
    reaction = ReactionTypeEmoji(emoji=choice(emos))
    await message.react([reaction])
    await bot.send_message(
        message.from_user.id,
        f'you are kurwa, mr {message.from_user.first_name}',
        reply_markup=main_keyboard
    )


@dp.message(Command('sector_kurwa'))
async def get_kurwa(message: Message):
    choice = await message.answer_dice(DiceEmoji.DART)
    await message.answer('Sector kurwa is on the drum')
    print(choice.dice.value)


@dp.message(F.text == 'Эмоджи')
async def get_smile(message: Message):
    await message.answer(text=emoji.emojize('☠'))


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
