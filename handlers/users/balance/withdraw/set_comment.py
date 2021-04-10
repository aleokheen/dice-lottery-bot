from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.regular.user import default_keyboard
from loader import bot, dp, db_users

from states.user import BalanceState


@dp.message_handler(chat_type="private", state=BalanceState.set_amount_for_withdraw, regexp=r"^\d+$")
async def set_amount_for_withdraw(message: types.Message, state: FSMContext):

    # Fetch user info
    user = await db_users.find_one({'id': message.from_user.id})

    # If cancel
    if message.text == '0':
        await state.reset_state()
        await message.answer('Вывод средств отменён', reply_markup=default_keyboard)
        return

    # If amount is not enough
    if int(message.text) < 100:
        return await message.answer('Вывести можно минимум 100 ₽')

    # If balance is not enough
    if user['balance'] - int(message.text) < 0:
        return await message.answer('Недостаточно средств')

    # Update state
    await BalanceState.set_comment_for_withdraw.set()
    await state.update_data(amount=int(message.text))

    # Send comment prompt message
    await message.answer(
        text=f'Опишите в свободной форме, куда зачислить ваши средства',
        reply_markup=ReplyKeyboardRemove()
    )
