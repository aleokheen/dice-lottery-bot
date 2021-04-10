from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.regular.user import default_keyboard
from loader import dp


@dp.message_handler(chat_type="private", state='*', text=['Назад', 'Отмена'])
async def show_balance(message: types.Message, state: FSMContext):

    await state.reset_state()

    await message.answer(
        text=f'Главное меню',
        reply_markup=default_keyboard
    )