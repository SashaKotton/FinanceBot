from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def get_phone(items):
    row = [KeyboardButton(text = item, request_contact=True) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)