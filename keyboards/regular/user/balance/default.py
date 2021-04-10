from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

balance_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Пополнить"),
            KeyboardButton(text="Вывести")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)