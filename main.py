import asyncio
import logging
import sys

from aiogram.enums import ParseMode
from dotenv import load_dotenv
import os
from aiogram import Bot
import handlers as ha
from aiogram.client.bot import DefaultBotProperties


load_dotenv()
TG_TOKEN = os.getenv('TOKEN')

bot = Bot(TG_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await ha.dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Program Interrupted')
