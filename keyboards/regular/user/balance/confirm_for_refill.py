from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

confirm_for_refill_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ага, готово!")
        ],
        [
            KeyboardButton(text="Отмена")
        ]
    ],
    resize_keyboard=True
)