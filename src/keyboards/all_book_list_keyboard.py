from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.lexicon.lexicon import LexiconRu
from src.keyboards.keyboard import KeyboardButtonBase
from src.constants import PAGE_SIZE_SHOW_ALL_BOOKS

BOOK_PAGE_PREFIX = "book_page:"


def create_pagination_book_keyboard(current_page: int, total_pages: int, curreny_elemnts: int, total_elements: int) -> InlineKeyboardMarkup:
    """
    Создаёт inline-кнопки для пагинации списка книг: << >> и В меню.
    """
    builder = InlineKeyboardBuilder()
    buttons = []

    if current_page > 0:
        buttons.append(
            InlineKeyboardButton(
                text=LexiconRu.BackPagination,
                callback_data=f"{BOOK_PAGE_PREFIX}{current_page - 1}",
            ),
        )
    if current_page < total_pages - 1:
        buttons.append(
            InlineKeyboardButton(
                text=LexiconRu.ForwardPagination,
                callback_data=f"{BOOK_PAGE_PREFIX}{current_page + 1}",
            )
        )
    if buttons:
        builder.row(*buttons)
        
    builder.row(
        InlineKeyboardButton(
            text=f"{curreny_elemnts + PAGE_SIZE_SHOW_ALL_BOOKS}/{total_elements}", 
            callback_data=KeyboardButtonBase.Stub),
    )
    
    builder.row(
        InlineKeyboardButton(
            text=LexiconRu.ToMenuButton,
            callback_data=KeyboardButtonBase.ToMenu,
        )
    )
    return builder.as_markup()
