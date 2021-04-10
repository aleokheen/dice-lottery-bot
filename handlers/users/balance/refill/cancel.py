import requests
from aiogram import types
from aiogram.dispatcher import FSMContext

from config import QIWI_P2P_PRIVKEY
from keyboards.regular.user import default_keyboard
from loader import bot, dp, db_users

from states.user import BalanceState


@dp.message_handler(chat_type="private", state=BalanceState.confirm_for_refill, text='Отмена')
async def cancel_refill(message: types.Message, state: FSMContext):

    # Reset state
    await state.reset_state()

    # Fetch user info
    user = await db_users.find_one({'id': message.from_user.id})

    # Delete qiwi bill id
    await db_users.update_one({'id': message.from_user.id}, {'$unset': {
        'billId': ''
    }})

    # Cancel qiwi invoice

    r = requests.post(
        url=f'https://api.qiwi.com/partner/bill/v1/bills/{user["billId"]}/reject',
        headers={
            'Authorization': f'Bearer {QIWI_P2P_PRIVKEY}',
            'Content-Type': 'application/json'
        },
        data={}
    )

    r.json()

    # Send message
    await message.answer(
        text=f'Пополнение баланса отменено. Если захотите пополнить, запросите новую платёжную ссылку',
        reply_markup=default_keyboard
    )
