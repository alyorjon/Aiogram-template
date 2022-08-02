import logging

from aiogram import Dispatcher
from loader import bot
# from data.config import ADMINS
from data.admin_idlar import adminlar


async def on_startup_notify(dp: Dispatcher):
    for admin in adminlar:
        try:
            await bot.send_message(chat_id=admin, text="Bot ishga tushdi")

        except Exception as err:
            logging.exception(err)
