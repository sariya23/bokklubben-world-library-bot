from aiogram import Router
from aiogram import F
from aiogram.types import CallbackQuery
from src.keyboards.profile_keyboard import create_profile_keyboard
from src.domain.profile import Profile
from src.lexicon.lexicon import LexiconRu
from src.domain.book import BookList
from src.keyboards.profile_keyboard import KeyboardButtonProfile
from src.keyboards.main_keyboard import KeyboardButton
from src.keyboards.profile_unreaded_book_keyboard import create_pagination_profile_unreaded_book_keyboard
from src.keyboards.profile_readed_book_keyboard import create_pagination_profile_readed_book_keyboard
from src.constants import PAGE_SIZE_PROFILE_READED_BOOKS, PAGE_SIZE_PROFILE_UNREADED_BOOKS
from src.keyboards.profile_readed_book_keyboard import PROFILE_READED_BOOK_PAGE_PREFIX
from src.keyboards.profile_unreaded_book_keyboard import PROFILE_UNREADED_BOOK_PAGE_PREFIX
from typing import Protocol
from aiogram.utils.formatting import Bold, as_list, as_marked_section

class ProfileService(Protocol):
    async def get_profile(self, user_id: int) -> Profile:
        pass

def _total_pages_show_profile_readed_books(total: int) -> int:
    return max(1, (total + PAGE_SIZE_PROFILE_READED_BOOKS - 1) // PAGE_SIZE_PROFILE_READED_BOOKS)


def _page_slice_show_profile_readed_books(books: BookList, page: int) -> BookList:
    start = page * PAGE_SIZE_PROFILE_READED_BOOKS
    return books[start : start + PAGE_SIZE_PROFILE_READED_BOOKS]

def _total_pages_show_profile_unreaded_books(total: int) -> int:
    return max(1, (total + PAGE_SIZE_PROFILE_UNREADED_BOOKS - 1) // PAGE_SIZE_PROFILE_UNREADED_BOOKS)

def _page_slice_show_profile_unreaded_books(books: BookList, page: int) -> BookList:
    start = page * PAGE_SIZE_PROFILE_UNREADED_BOOKS
    return books[start : start + PAGE_SIZE_PROFILE_UNREADED_BOOKS]


def create_router(profile_service: ProfileService) -> Router:
    router = Router()
    
    @router.callback_query(F.data == KeyboardButton.Profile)
    async def process_profile(callback: CallbackQuery):
        profile = await profile_service.get_profile(callback.from_user.id)
        await callback.message.edit_text(**LexiconRu.build_profile_text(
            profile),
            reply_markup=create_profile_keyboard(
                len(profile.total_readed_books),
                len(profile.total_unreaded_books),
            ))
        await callback.answer()
    
    async def _reply_profile_readed_book_page(callback: CallbackQuery, page: int):
        user_id = callback.from_user.id
        profile = await profile_service.get_profile(user_id)
        total_pages = _total_pages_show_profile_readed_books(len(profile.total_readed_books))
        page = max(0, min(page, total_pages - 1))
        chunk = _page_slice_show_profile_readed_books(profile.total_readed_books, page)
        elements = [f"{book.author} — {book.title}" for book in chunk]
        if not elements:
            callback.answer()
            return 
        content = as_list(
            as_marked_section(
                Bold("📚", "Список прочитанных книг\n"),
                *elements,
                marker="📗",
            )
        )
        keyboard = create_pagination_profile_readed_book_keyboard(page, total_pages, PAGE_SIZE_PROFILE_READED_BOOKS * page, len(profile.total_readed_books))
        await callback.message.edit_text(
            **content.as_kwargs(),
            reply_markup=keyboard,
        )
        await callback.answer()
    
    async def _reply_profile_unreaded_book_page(callback: CallbackQuery, page: int):
        user_id = callback.from_user.id
        profile = await profile_service.get_profile(user_id)
        total_pages = _total_pages_show_profile_unreaded_books(len(profile.total_unreaded_books))
        page = max(0, min(page, total_pages - 1))
        chunk = _page_slice_show_profile_unreaded_books(profile.total_unreaded_books, page)
        elements = [f"{book.author} — {book.title}" for book in chunk]
        if not elements:
            callback.answer()
            return 
        content = as_list(
            as_marked_section(
                Bold("📚", "Список непрочитанных книг\n"),
                *elements,
                marker="📕",
            )
        )
        keyboard = create_pagination_profile_unreaded_book_keyboard(page, total_pages, PAGE_SIZE_PROFILE_UNREADED_BOOKS * page, len(profile.total_unreaded_books))
        await callback.message.edit_text(
            **content.as_kwargs(),
            reply_markup=keyboard,
        )
        await callback.answer()

    @router.callback_query(F.data.startswith(PROFILE_UNREADED_BOOK_PAGE_PREFIX))
    async def process_unreaded_book_page(callback: CallbackQuery):
        try:
            page = int(callback.data.removeprefix(PROFILE_UNREADED_BOOK_PAGE_PREFIX))
        except ValueError:
            await callback.answer()
            return
        await _reply_profile_unreaded_book_page(callback, page)

    @router.callback_query(F.data.startswith(PROFILE_READED_BOOK_PAGE_PREFIX))
    async def process_readed_book_page(callback: CallbackQuery):
        try:
            page = int(callback.data.removeprefix(PROFILE_READED_BOOK_PAGE_PREFIX))
        except ValueError:
            await callback.answer()
            return
        await _reply_profile_readed_book_page(callback, page)
    
    @router.callback_query(F.data == KeyboardButtonProfile.ReadedBooks)
    async def process_readed_books(callback: CallbackQuery):
        await _reply_profile_readed_book_page(callback, 0)
    
    @router.callback_query(F.data == KeyboardButtonProfile.UnreadedBooks)
    async def process_unreaded_books(callback: CallbackQuery):
        await _reply_profile_unreaded_book_page(callback, 0)
    
    return router