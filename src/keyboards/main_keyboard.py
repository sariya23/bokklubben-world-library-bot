from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

class KeyboardButton:
    ShowAllBookList = "show_all_book_list"
    MarkAlreadyReaded = "mark_already_readed"


button_show_all_book_list = InlineKeyboardButton(
    text="Книги Всемирной библиотеки",
    callback_data=KeyboardButton.ShowAllBookList
)

button_mark_already_readed = InlineKeyboardButton(
    text="Отметить прочитанные книги",
    callback_data=KeyboardButton.MarkAlreadyReaded
)

keyboard_main = InlineKeyboardMarkup(
    inline_keyboard=[[button_show_all_book_list, button_mark_already_readed]]
)