from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

class KeyboardButton:
    ShowAllBookList = "show_all_book_list"


button_show_all_book_list = InlineKeyboardButton(
    text="Книги Всемирной библиотеки",
    callback_data=KeyboardButton.ShowAllBookList
)

keyboard_main = InlineKeyboardMarkup(
    inline_keyboard=[[button_show_all_book_list]]
)