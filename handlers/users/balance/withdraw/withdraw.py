from aiogram import types
from aiogram.dispatcher import FSMContext

from config import ADMIN_CHAT_ID
from keyboards.regular.user import default_keyboard
from loader import bot, dp, db_users
from states.user import BalanceState


@dp.message_handler(chat_type="private", state=BalanceState.set_comment_for_withdraw, regexp=r".{10,}$")
async def withdraw(message: types.Message, state: FSMContext):

    # Fetch data from state

    state_data = await state.get_data()
    amount = state_data.get('amount')

    # Fetch user info
    user = await db_users.find_one({'id': message.from_user.id})

    # Update balance
    await db_users.update_one(user, {'$inc': {
        'balance': -amount
    }})

    # Reset state
    await state.reset_state()

    # Send message
    await message.answer(
        text=f'Заявка на вывод средств принята',
        reply_markup=default_keyboard
    )

    # Send admin message
    await bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f'<b>Заявка на вывод средств</b>\n\n'
             f'<b>Сумма:</b> {amount} ₽\n'
             f'<b>Пользователь:</b> @{user["username"] or "None"} / {user["id"]}\n'
             f'<b>Баланс:</b> {user["balance"]}\n\n'
             f'<b>Комментарий:</b>\n{message.text}'
    )
