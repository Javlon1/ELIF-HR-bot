from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_delete = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('/delete')
        ],
    ]
)


kb_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('/menu'),
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)