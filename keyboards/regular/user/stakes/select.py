from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

select_stake_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1. Чётное / Нечётное")
        ],
        [
            KeyboardButton(text="2. Делится на 3")
        ],
        [
            KeyboardButton(text="3. Конкретное число")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)