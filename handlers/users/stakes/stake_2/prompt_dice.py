from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp, db_users
from states.user.stake import StakeState


@dp.message_handler(chat_type="private", state=StakeState.select, text_contains='2')
async def stake_2_prompt_dice(message: types.Message):

    # Fetch user info
    user = await db_users.find_one({'id': message.from_user.id})

    # Charge balance
    await db_users.update_one(user, {'$inc': {
        'balance': -25
    }})

    # Change state
    await StakeState.stake_2_prompt_dice.set()

    # Send dice prompt message
    await message.answer(
        text=f'Делайте ставку, {message.from_user.first_name}',
        reply_markup=ReplyKeyboardMarkup(keyboard=[
            [
                KeyboardButton(text='🎲'),
                KeyboardButton(text='Отмена')
            ]
        ], resize_keyboard=True)
    )