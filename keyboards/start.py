from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def make_keyboard(items):
    row = [KeyboardButton(text = item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)