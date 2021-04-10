from aiogram import types

from funcs import generate_random_string
from config import QIWI_P2P_PUBKEY
from keyboards.regular.user import confirm_for_refill_keyboard
from loader import dp, db_users

from states.user import BalanceState


@dp.message_handler(chat_type="private", state=BalanceState.show, text='Пополнить')
async def confirm_for_refill(message: types.Message):

    # Change state
    await BalanceState.confirm_for_refill.set()

    # Generate qiwi bill id

    bill_id = generate_random_string(16)

    await db_users.update_one({'id': message.from_user.id}, {'$set': {
        'billId': bill_id
    }})

    # Send message
    await message.answer(
        text=f'Для пополнения баланса перейдите на сайт платёжной системы:\n\n'
             f'<a href="https://oplata.qiwi.com/create?publicKey={QIWI_P2P_PUBKEY}&billId={bill_id}">Ссылка для оплаты</a>\n\n'
             f'После успешного проведения оплаты, нажмите кнопку "Ага, готово!"',
        reply_markup=confirm_for_refill_keyboard
    )
