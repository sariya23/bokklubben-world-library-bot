from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from src.lexicon.lexicon import LexiconRu
from src.keyboards.keyboard import KeyboardButtonBase
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.domain.book import Book
from src.constants import PAGE_SIZE_MARK_READED

MARK_READED_PAGE_PREFIX = "mark_readed_page:"


def generate_mark_readed_books_keyboard(
    books: list[Book],
    current_page: int = 0,
    total_pages: int = 1,
    total_elements: int = 0,
    readed_book_ids: set[int] | None = None,
) -> InlineKeyboardMarkup:
    if readed_book_ids is None:
        readed_book_ids = set()
    builder = InlineKeyboardBuilder()
    for book in books:
        label = f"{book.title} - {book.author}"
        if book.id in readed_book_ids:
            label = f"{LexiconRu.BookMarkedAsReaded} {label}"
        builder.row(
            InlineKeyboardButton(
                text=label,
                callback_data=f"mark_readed_book:{book.id}:{current_page}",
            )
        )
    nav_buttons = []
    if current_page > 0:
        nav_buttons.append(
            InlineKeyboardButton(
                text=LexiconRu.BackPagination,
                callback_data=f"{MARK_READED_PAGE_PREFIX}{current_page - 1}",
            )
        )
    if current_page < total_pages - 1:
        nav_buttons.append(
            InlineKeyboardButton(
                text=LexiconRu.ForwardPagination,
                callback_data=f"{MARK_READED_PAGE_PREFIX}{current_page + 1}",
            )
        )
    if nav_buttons:
        builder.row(*nav_buttons)
    shown = min((current_page + 1) * PAGE_SIZE_MARK_READED, total_elements)
    if total_elements > 0:
        builder.row(
            InlineKeyboardButton(
                text=f"{shown}/{total_elements}",
                callback_data=KeyboardButtonBase.Stub,
            )
        )
    builder.row(
        InlineKeyboardButton(
            text=LexiconRu.ToMenuButton,
            callback_data=KeyboardButtonBase.ToMenu,
        )
    )
    return builder.as_markup()