from create_bot import bot, Dispatcher
from aiogram import types
from data__base import sqlite_db
from Keyboards.kb_admin import kb_admin

    
KEY = None


#получаем ID текущего модератора
# @dp.message_handler(commands=[KEY], is_chat_admin=True)
async def get_admin(message: types.Message):
    global KEY
    KEY = message.from_user.id
    await bot.send_message(message.from_user.id, 'добро пожаловать админ', reply_markup=kb_admin)


async def menu(message: types.Message):
    if message.from_user.id == KEY:
        await sqlite_db.sql_read(message)


# рег хендлеров
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(get_admin, commands=["Elifanketabaza"], is_chat_admin=True)       
    dp.register_message_handler(menu, commands=['Elifanketamenu'])