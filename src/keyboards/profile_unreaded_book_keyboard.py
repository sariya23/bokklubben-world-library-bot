from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.lexicon.lexicon import LexiconRu
from src.keyboards.keyboard import KeyboardButtonBase
from src.constants import PAGE_SIZE_PROFILE_UNREADED_BOOKS
from src.keyboards.main_keyboard import button_profile

PROFILE_UNREADED_BOOK_PAGE_PREFIX = "profile_unreaded_book_page:"

def create_pagination_profile_unreaded_book_keyboard(current_page: int, total_pages: int, curreny_elemnts: int, total_elements: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    buttons = []

    if current_page > 0:
        buttons.append(
            InlineKeyboardButton(
                text=LexiconRu.BackPagination,
                callback_data=f"{PROFILE_UNREADED_BOOK_PAGE_PREFIX}{current_page - 1}",
            ),
        )
    if current_page < total_pages - 1:
        buttons.append(
            InlineKeyboardButton(
                text=LexiconRu.ForwardPagination,
                callback_data=f"{PROFILE_UNREADED_BOOK_PAGE_PREFIX}{current_page + 1}",
            )
        )
    if buttons:
        builder.row(*buttons)
        
    builder.row(
        InlineKeyboardButton(
            text=f"{min(curreny_elemnts + PAGE_SIZE_PROFILE_UNREADED_BOOKS, total_elements)}/{total_elements}", 
            callback_data=KeyboardButtonBase.Stub),
    )
    
    builder.row(
        button_profile
    )
    return builder.as_markup()
