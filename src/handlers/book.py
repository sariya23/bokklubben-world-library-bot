from src.keyboards.main_keyboard import KeyboardButton
from src.keyboards.all_book_list_keyboard import (
    create_pagination_book_keyboard,
    BOOK_PAGE_PREFIX,
)
from src.keyboards.mark_readed_books_keyboard import (
    generate_mark_readed_books_keyboard,
    MARK_READED_PAGE_PREFIX,
)
from src.lexicon.lexicon import LexiconRu
from typing import Protocol
from aiogram import Router
from aiogram.utils.formatting import Bold, as_list, as_marked_section
from aiogram import F
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from src.domain.book import Book
from src.constants import PAGE_SIZE_SHOW_ALL_BOOKS, PAGE_SIZE_MARK_READED


class BookService(Protocol):
    async def get_all_books(self) -> list[Book]:
        pass
    async def mark_readed_book(self, book_id: int):
        pass


def _total_pages_show_all_books(total: int) -> int:
    return max(1, (total + PAGE_SIZE_SHOW_ALL_BOOKS - 1) // PAGE_SIZE_SHOW_ALL_BOOKS)

def _total_pages_mark_readed_books(total: int) -> int:
    return max(1, (total + PAGE_SIZE_MARK_READED - 1) // PAGE_SIZE_MARK_READED)


def _page_slice_show_all_books(books: list[Book], page: int) -> list[Book]:
    start = page * PAGE_SIZE_SHOW_ALL_BOOKS
    return books[start : start + PAGE_SIZE_SHOW_ALL_BOOKS]

def _page_slice_mark_readed_books(books: list[Book], page: int) -> list[Book]:
    start = page * PAGE_SIZE_MARK_READED
    return books[start : start + PAGE_SIZE_MARK_READED]


def create_router(book_service: BookService) -> Router:
    router = Router()

    async def _reply_book_page(callback: CallbackQuery, page: int):
        books = await book_service.get_all_books()
        total_pages = _total_pages_show_all_books(len(books))
        page = max(0, min(page, total_pages - 1))
        chunk = _page_slice_show_all_books(books, page)
        elements = [f"{book.author} — {book.title}" for book in chunk]
        content = as_list(
            as_marked_section(
                Bold("📚", "Список книг\n"),
                *elements,
                marker="📕",
            )
        )
        keyboard = create_pagination_book_keyboard(page, total_pages, PAGE_SIZE_SHOW_ALL_BOOKS * page, len(books))
        await callback.message.edit_text(
            **content.as_kwargs(),
            reply_markup=keyboard,
        )
        await callback.answer()

    @router.callback_query(F.data == KeyboardButton.ShowAllBookList)
    async def process_show_all_book_list(callback: CallbackQuery):
        await _reply_book_page(callback, 0)

    @router.callback_query(F.data.startswith(BOOK_PAGE_PREFIX))
    async def process_book_page(callback: CallbackQuery):
        try:
            page = int(callback.data.removeprefix(BOOK_PAGE_PREFIX))
        except ValueError:
            await callback.answer()
            return
        await _reply_book_page(callback, page)
    
    async def _reply_mark_readed_page(callback: CallbackQuery, page: int):
        books = await book_service.get_all_books()
        total_pages = _total_pages_mark_readed_books(len(books))
        page = max(0, min(page, total_pages - 1))
        chunk = _page_slice_mark_readed_books(books, page)
        keyboard = generate_mark_readed_books_keyboard(
            chunk, current_page=page, total_pages=total_pages, total_elements=len(books)
        )
        try:
            await callback.message.edit_text(**LexiconRu.MarkAlreadyReaded, reply_markup=keyboard)
        except TelegramBadRequest as e:
            if "message is not modified" not in str(e):
                raise

    @router.callback_query(F.data == KeyboardButton.MarkAlreadyReaded)
    async def process_mark_already_readed(callback: CallbackQuery):
        await _reply_mark_readed_page(callback, 0)
        await callback.answer()

    @router.callback_query(F.data.startswith(MARK_READED_PAGE_PREFIX))
    async def process_mark_readed_page(callback: CallbackQuery):
        try:
            page = int(callback.data.removeprefix(MARK_READED_PAGE_PREFIX))
        except ValueError:
            await callback.answer()
            return
        await _reply_mark_readed_page(callback, page)
        await callback.answer()

    @router.callback_query(F.data.startswith("mark_readed_book:"))
    async def process_mark_readed_book(callback: CallbackQuery):
        parts = callback.data.removeprefix("mark_readed_book:").split(":")
        if len(parts) < 2:
            await callback.answer()
            return
        try:
            book_id = int(parts[0])
            page = int(parts[1])
        except ValueError:
            await callback.answer()
            return
        user_id = callback.from_user.id
        await book_service.mark_readed_book(book_id, user_id)
        await _reply_mark_readed_page(callback, page)
        await callback.answer(LexiconRu.BookMarkedAsReaded)

    return router