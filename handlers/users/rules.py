from aiogram import types
from loader import bot, dp, db_users


@dp.message_handler(chat_type="private", state=None, text_contains='Правила')
async def show_rules(message: types.Message):

    await message.answer(
        text=f'<b>❗ Правила ❗</b>\n\n'
             f'Данный бот сделан не для широкой аудитории и создан исключительно '
             f'в целях демонстрации навыков его разработчика.\n\n'
             f'<b>Минимальное количество средств для вывода:</b> 100 ₽\n\n'
             f'Запросы на вывод средств могут быть проигнорированы без объяснения причин'
    )