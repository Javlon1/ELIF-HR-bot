from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_delete = KeyboardButton('/delete')


kb_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('/Elifanketamenu'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)