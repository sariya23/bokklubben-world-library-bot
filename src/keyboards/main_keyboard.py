from aiogram.types import (
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

class KeyboardButton:
    ShowAllBookList = "show_all_book_list"
    MarkAlreadyReaded = "mark_already_readed"
    Profile = "profile"
    RandomBook = "random_book"


button_show_all_book_list = InlineKeyboardButton(
    text="📚 Книги Всемирной библиотеки",
    callback_data=KeyboardButton.ShowAllBookList
)

button_mark_already_readed = InlineKeyboardButton(
    text="📋 Отметить прочитанные книги",
    callback_data=KeyboardButton.MarkAlreadyReaded
)

button_profile = InlineKeyboardButton(
    text="🙍‍♂️ Профиль",
    callback_data=KeyboardButton.Profile
)

button_random_book = InlineKeyboardButton(
    text="🎲 Случайная книга",
    callback_data=KeyboardButton.RandomBook
)

keyboard_main = InlineKeyboardBuilder()
keyboard_main.row(button_show_all_book_list, button_mark_already_readed)
keyboard_main.row(button_profile)
keyboard_main.row(button_random_book)