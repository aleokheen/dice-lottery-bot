from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp, db_users
from states.user.stake import StakeState


@dp.message_handler(chat_type="private", state=StakeState.stake_3_prompt_case, regexp=r"^[1-6]$")
async def stake_3_prompt_dice(message: types.Message, state: FSMContext):

    # Fetch user info
    user = await db_users.find_one({'id': message.from_user.id})

    # Change state
    await StakeState.stake_3_prompt_dice.set()
    await state.update_data(case=int(message.text))

    # Send prompt message
    await message.answer(
        text=f'Делайте ставку, {message.from_user.first_name}',
        reply_markup=ReplyKeyboardMarkup(keyboard=[
            [
                KeyboardButton(text='🎲'),
                KeyboardButton(text='Отмена')
            ]
        ], resize_keyboard=True)
    )
