from aiogram import types
from loader import dp
from config import ADMIN_CHAT_ID


@dp.message_handler(commands='start', chat_type="group", chat_id=ADMIN_CHAT_ID)
async def bot_start(message: types.Message):
    await message.answer(f"Админка!")