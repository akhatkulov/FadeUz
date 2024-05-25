from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def start_key():
    x = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text="🗒Navbat olish",callback_data="navbat_ol")
    x.add(btn1)
    btn2 = InlineKeyboardButton(text="🧑Sartarosh haqida",callback_data="sartarosh")
    btn3 = InlineKeyboardButton(text="📍Manzil",callback_data="manzil")
    x.add(btn2,btn3)
    return x