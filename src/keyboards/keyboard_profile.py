from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.keyboards.keyboard import KeyboardButtonBase
from src.lexicon.lexicon import LexiconRu
from aiogram.types import InlineKeyboardButton

class KeyboardButtonProfile:
    ReadedBooks = "readed_books"
    UnreadedBooks = "unreaded_books"

keyboard_profile = InlineKeyboardBuilder()

readed_books = InlineKeyboardButton(
    text="🟢 Прочитанные книги",
    callback_data=KeyboardButtonProfile.ReadedBooks,
)

unreaded_books = InlineKeyboardButton(
    text="🔴 Осталось прочитать",
    callback_data=KeyboardButtonProfile.UnreadedBooks,
)

keyboard_profile.add(readed_books, unreaded_books)

keyboard_profile.row(
    InlineKeyboardButton(
        text=LexiconRu.ToMenuButton,
        callback_data=KeyboardButtonBase.ToMenu,
    )
)

