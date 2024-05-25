from aiogram import types

from loader import dp,bot
from aiogram.dispatcher import FSMContext
from utils.db_api.db import *

support_id = 789945598

@dp.callback_query_handler(text="sartarosh")
async def sartarosh_info(call: types.CallbackQuery):
    await bot.send_photo(chat_id=call.message.chat.id,photo="https://t.me/Unabi_SS/31726",caption="Sartarosh haqida ma'lumotlar")

dp.callback_query_handler(text="manzil")
async def manzil(call: types.CallbackQuery):
    longitude=66.919773
    latitude=39.633713
    await bot.send_location(chat_id=call.message.chat.id, latitude=latitude, longitude=longitude)
    await call.answer()

@dp.callback_query_handler(text="navbat_ol")
async def navbat_ol(call: types.CallbackQuery,state: FSMContext):
    await call.message.answer("Ismingizni yuboring")
    await state.set_state("ism_ol")

@dp.message_handler(state="ism_ol")
async def ism_ol(message: types.Message,state : FSMContext):
    put_name(cid=message.chat.id,name=message.text)
    await message.answer("Telefon raqamingizni yuboring")
    await state.set_state("tel_ol")

@dp.message_handler(state="tel_ol")
async def tel_ol(message:types.Message,state: FSMContext):
    put_tel(cid=message.chat.id,tel=message.text)
    await message.answer("Navbatni qachonga olmoqchisiz?")
    await state.set_state("kun_ol")

@dp.message_handler(state="kun_ol")
async def kun_ol(message: types.Message, state: FSMContext):
    put_nav(cid=message.chat.id,nav=message.text)
    await message.answer("👌Adminga yuborildi, siz bilan tez orada aloqaga chiqiladi")
    x = f"👌Yangi buyurtma!\n🧑Ismi: {get_name(message.chat.id)},\n📱Raqami: {get_tel(message.chat.id)}\n📅Qachonga navbat: {get_nav(message.chat.id)}"
    await bot.send_message(chat_id=support_id,text=x)
    await state.finish()
