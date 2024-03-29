import asyncio
import logging
import sys

from dotenv import load_dotenv
import os
from aiogram import Bot
import handlers as ha


load_dotenv()
TG_TOKEN = os.getenv('TOKEN')

bot = Bot(TG_TOKEN)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await ha.dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Program Interrupted')
