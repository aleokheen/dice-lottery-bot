import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.regular.user import default_keyboard
from loader import dp, db_users
from states.user.stake import StakeState


@dp.message_handler(chat_type="private", state=StakeState.stake_1_prompt_dice, content_types='dice', is_forwarded=False)
async def stake_1(message: types.Message, state: FSMContext):

    # Fetch state data

    state_data = await state.get_data()
    case = state_data.get('case')

    # Fetch dice value
    value = message.dice.value

    # Reset state
    await state.reset_state()

    # Wait for 4 seconds (during dice animation)
    await asyncio.sleep(4)

    # Do stake
    if case == 'Чётное' and value % 2 == 0 or case == 'Нечётное' and value % 2 == 1:

        # Update balance
        await db_users.update_one({'id': message.from_user.id}, {'$inc': {
            'balance': 25 + 50
        }})

        # Send congrats message
        return await message.answer(
            text=f'🔥 Вы выиграли 50 ₽',
            reply_markup=default_keyboard
        )

    # Failure

    # Pay for referrals
    await db_users.update_one({'invitedUsers': message.from_user.id}, {'$inc': {
        'balance': 25 * 0.3
    }})

    # Send failure message
    await message.answer('Вы ничего не выиграли', reply_markup=default_keyboard)
