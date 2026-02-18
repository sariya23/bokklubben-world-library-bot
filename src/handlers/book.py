from src.keyboards.main_keyboard import KeyboardButton
from src.keyboards.all_book_list_keyboard import (
    create_pagination_book_keyboard,
    BOOK_PAGE_PREFIX,
)
from typing import Protocol
from aiogram import Router
from aiogram.utils.formatting import Bold, as_list, as_marked_section
from aiogram import F
from aiogram.types import CallbackQuery
from src.domain.book import Book
from src.constants import PAGE_SIZE_SHOW_ALL_BOOKS


class BookService(Protocol):
    async def get_all_books(self) -> list[Book]:
        pass


def _total_pages(total: int) -> int:
    return max(1, (total + PAGE_SIZE_SHOW_ALL_BOOKS - 1) // PAGE_SIZE_SHOW_ALL_BOOKS)


def _page_slice(books: list[Book], page: int) -> list[Book]:
    start = page * PAGE_SIZE_SHOW_ALL_BOOKS
    return books[start : start + PAGE_SIZE_SHOW_ALL_BOOKS]


def create_router(book_service: BookService) -> Router:
    router = Router()

    async def _reply_book_page(callback: CallbackQuery, page: int):
        books = await book_service.get_all_books()
        total_pages = _total_pages(len(books))
        page = max(0, min(page, total_pages - 1))
        chunk = _page_slice(books, page)
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

    return router