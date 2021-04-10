from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp, db_users
from states.user.stake import StakeState


@dp.message_handler(chat_type="private", state=StakeState.select, text_contains='3')
async def stake_3_prompt_1(message: types.Message):

    # Fetch user info
    user = await db_users.find_one({'id': message.from_user.id})

    # Charge balance
    await db_users.update_one(user, {'$inc': {
        'balance': -25
    }})

    # Change state
    await StakeState.stake_3_prompt_case.set()

    # Send prompt message
    await message.answer(
        text=f'Введите число 1-6',
        reply_markup=ReplyKeyboardMarkup(keyboard=[
            [
                KeyboardButton(text='1'),
                KeyboardButton(text="2"),
                KeyboardButton(text="3"),
                KeyboardButton(text="4"),
                KeyboardButton(text="5"),
                KeyboardButton(text="6"),
            ]
        ], resize_keyboard=True)
    )
