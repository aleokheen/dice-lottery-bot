from config import BOT_TOKEN, DB_URI

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2

import motor.motor_asyncio

# Prepare bot
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = RedisStorage2(prefix="dice_lottery_bot")
dp = Dispatcher(bot, storage=storage)

# Prepare database

db_client = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
db = db_client['dice_lottery']

db_users = db['users']
