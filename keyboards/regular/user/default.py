from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤑 Сделать ставку 🤑")
        ],
        [
            KeyboardButton(text="💲 Баланс 💲"),
            KeyboardButton(text="❗ Правила ❗")
        ],
        [
            KeyboardButton(text="💰 Реферальная система 💰")
        ]
    ],
    resize_keyboard=True
)