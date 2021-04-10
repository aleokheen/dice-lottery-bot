from aiogram import types
from loader import bot, dp, db_users


@dp.message_handler(chat_type="private", state=None, text_contains='Реферальная')
async def show_about_referral(message: types.Message):

    # Fetch user info
    user = await db_users.find_one({'id': message.from_user.id})

    # Fetch bot info
    bot_info = await bot.get_me()

    # Send message
    await message.answer(
        text=f'<b>💰 Реферальная система 💰</b>\n\n'
             f'Вы будете получать 30% с проигрышей пользователей, зарегистрированных по этой ссылке:\n\n'
             f't.me/{bot_info.username}?start={user["refCode"]}\n\n'
             f'Средства будут автоматически зачисляться на ваш баланс',
        disable_web_page_preview=True
    )
