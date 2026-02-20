from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.keyboards.keyboard import KeyboardButtonBase
from src.lexicon.lexicon import LexiconRu
from aiogram.types import InlineKeyboardButton

class KeyboardButtonProfile:
    ReadedBooks = "readed_books"
    UnreadedBooks = "unreaded_books"


def create_profile_keyboard(readed_count: int, unreaded_count: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    readed_books = InlineKeyboardButton(
        text="🟢 Прочитанные книги",
        callback_data=KeyboardButtonBase.Stub if readed_count == 0 else KeyboardButtonProfile.ReadedBooks,
    )
    unreaded_books = InlineKeyboardButton(
        text="🔴 Осталось прочитать",
        callback_data=KeyboardButtonBase.Stub if unreaded_count == 0 else KeyboardButtonProfile.UnreadedBooks,
    )
    builder.add(readed_books, unreaded_books)
    builder.row(
        InlineKeyboardButton(
            text=LexiconRu.ToMenuButton,
            callback_data=KeyboardButtonBase.ToMenu,
        )
    )
    return builder.as_markup()

