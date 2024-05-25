from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.start_keyboard import start_key
from loader import dp
from utils.db_api.db import create_user

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    create_user(message.chat.id)
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=start_key())
