from aiogram import types

from keyboards.regular.user import balance_default_keyboard
from loader import bot, dp, db_users

from states.user import BalanceState


@dp.message_handler(chat_type="private", state=None, text_contains='Баланс')
async def show_balance(message: types.Message):

    await BalanceState.show.set()

    user = await db_users.find_one({'id': message.from_user.id})

    await message.answer(
        text=f'<b>Ваш баланс</b>: {user["balance"]} ₽',
        reply_markup=balance_default_keyboard
    )
