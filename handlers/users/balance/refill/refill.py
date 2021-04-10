import requests
from aiogram import types
from aiogram.dispatcher import FSMContext

from config import QIWI_P2P_PRIVKEY, ADMIN_CHAT_ID
from keyboards.regular.user import default_keyboard
from loader import bot, dp, db_users

from states.user import BalanceState


@dp.message_handler(chat_type="private", state=BalanceState.confirm_for_refill, text='Ага, готово!')
async def refill(message: types.Message, state: FSMContext):

    # Fetch user info
    user = await db_users.find_one({'id': message.from_user.id})

    # Get refill status

    r = requests.get(f'https://api.qiwi.com/partner/bill/v1/bills/{user["billId"]}', headers={
        'Authorization': f'Bearer {QIWI_P2P_PRIVKEY}'
    })

    refill_status = r.json()

    # If not success
    if r.status_code > 400 or refill_status['status']['value'] != 'PAID':
        return await message.answer('Мы не видим зачисления средств')

    # Update balance and unset qiwi bill id
    await db_users.update_one({'id': message.from_user.id}, {
        '$inc': {
            'balance': refill_status['amount']['value']
        },
        '$unset': {
            'billId': ''
        }
    })

    # Reset state
    await state.reset_state()

    # Send message
    await message.answer(
        text=f'✔️Баланс пополнен!',
        reply_markup=default_keyboard
    )

    # Send admin message
    await bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f'<b>Пополнение баланса</b>\n\n'
             f'<b>Сумма:</b> {refill_status["amount"]["value"]} ₽\n'
             f'<b>Пользователь:</b> @{user["username"] or "None"} / {user["id"]}\n'
             f'<b>Новый баланс:</b> {user["balance"] + refill_status["amount"]["value"]}'
    )
