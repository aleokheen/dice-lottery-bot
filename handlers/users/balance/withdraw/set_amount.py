from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from loader import dp

from states.user import BalanceState


@dp.message_handler(chat_type="private", state=BalanceState.show, text='Вывести')
async def set_withdraw_amount(message: types.Message):

    # Set state
    await BalanceState.set_amount_for_withdraw.set()

    # Send message prompt
    await message.answer(
        text=f'Введите количество средств для вывода.\n\n'
             f'Для отмены введите: 0',
        reply_markup=ReplyKeyboardRemove()
    )
