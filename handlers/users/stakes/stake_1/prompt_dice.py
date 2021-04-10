from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp, db_users
from states.user.stake import StakeState


@dp.message_handler(chat_type="private", state=StakeState.stake_1_prompt_case, text=['Чётное', 'Нечётное'])
async def stake_1_prompt_dice(message: types.Message, state: FSMContext):

    # Fetch user info
    user = await db_users.find_one({'id': message.from_user.id})

    # Change state
    await StakeState.stake_1_prompt_dice.set()
    await state.update_data(case=message.text)

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