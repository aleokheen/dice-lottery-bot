from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp, db_users
from states.user.stake import StakeState


@dp.message_handler(chat_type="private", state=StakeState.select, text_contains='1')
async def stake_1_prompt_case(message: types.Message):

    # Fetch user info
    user = await db_users.find_one({'id': message.from_user.id})

    # Charge balance
    await db_users.update_one(user, {'$inc': {
        'balance': -25
    }})

    # Change state
    await StakeState.stake_1_prompt_case.set()

    # Send case prompt message
    await message.answer(
        text=f'Выберите вариант ставки',
        reply_markup=ReplyKeyboardMarkup(keyboard=[
            [
                KeyboardButton(text='Чётное'),
                KeyboardButton(text="Нечётное")
            ]
        ], resize_keyboard=True)
    )