from datetime import datetime
from aiogram import types

from funcs import generate_random_string
from config import ADMIN_CHAT_ID
from keyboards.regular.user import default_keyboard
from loader import bot, dp, db_users


@dp.message_handler(commands='start', chat_type="private")
async def bot_start(message: types.Message):

    # Check if user exists
    if await db_users.count_documents({'id': message.from_user.id}):
        return await message.answer('❌ Вы уже начинали диалог с этим ботом', reply_markup=default_keyboard)

    # Save user into into db
    await db_users.insert_one({
        'id': message.from_user.id,
        'firstName': message.from_user.first_name,
        'lastName': message.from_user.last_name,
        'username': message.from_user.username,
        'createdAt': datetime.now(),
        'balance': 25,
        'refCode': generate_random_string(8)
    })

    # Do referral

    ref_code = message.text[7:]

    if ref_code:
        await db_users.find_one({'refCode': ref_code}, {'$addToSet': {
            'invitedUsers': message.from_user.id
        }})

    # Send welcome message
    await message.answer(
        text=f'Добро пожаловать, {message.from_user.first_name}!\n\n'
             f'<b>Твой баланс:</b> 25 ₽\n\n',
        reply_markup=default_keyboard
    )

    # Send message to admins
    await bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f'<b>Новый пользователь</b>\n\n'
             f'Имя: {message.from_user.full_name}\n'
             f'Ник: @{message.from_user.username if message.from_user.username else "none"}'
    )