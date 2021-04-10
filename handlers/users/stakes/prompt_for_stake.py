from aiogram import types

from keyboards.regular.user import select_stake_keyboard
from loader import bot, dp, db_users
from states.user.stake import StakeState


@dp.message_handler(chat_type="private", state=None, text_contains='Сделать ставку')
async def prompt_for_stake(message: types.Message):

    # Fetch user info
    user = await db_users.find_one({'id': message.from_user.id})

    # Check balance
    if user['balance'] < 25:
        return await message.answer('Недостаточно средств для совершения ставки. Нужно минимум 25 ₽')

    # Change state
    await StakeState.select.set()

    # Send prompt messages

    await message.answer(
        text=f'Вы бросите игральную кость (виртуальную). '
             f'Никто не знает, какой номинал выпадет; поэтому мы предлагаем вам сделать ставку.\n\n'
             f'Если угадаете с выбором, вы выиграете средства, которые сможете потом вывести.\n\n'
             f'<b>Базовая стоимость ставки:</b> 25 ₽\n\n'
             f'<b>У вас есть:</b> {user["balance"]} ₽'
    )

    await message.answer(
        text=f'<b>Варианты ставки</b>\n\n'
             f'<b>1. Чётное / Нечётное</b> - номинал кости - чётное (2,4,6) или нечётное (1,3,5) число.\n'
             f'Коэффициент: 2/1 (вознаграждение 50 ₽)'
             f'\n\n'
             f'<b>2. Делится на 3</b> - номинал кости делится на 3 (является числом 3 или 6).\n'
             f'Коэффициент: 4/1 (вознаграждение 100 ₽)'
             f'\n\n'
             f'<b>3. Конкретное число</b> - вы выбираете конкретное число, которое выпадет.\n'
             f'Коэффициент: 6/1 (вознаграждение 150 ₽)',
        reply_markup=select_stake_keyboard
    )