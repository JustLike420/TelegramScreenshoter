# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
main_menu_inl = InlineKeyboardMarkup(
).add(
    InlineKeyboardButton(text="Сделать скриншот", callback_data=f"screenshot")
)
