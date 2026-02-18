from src.keyboards.main_keyboard import KeyboardButton
from typing import Protocol
from aiogram import Router
from aiogram.utils.formatting import Bold, as_list, as_marked_section
from aiogram import F
from aiogram.types import CallbackQuery
from src.domain.book import Book

class BookService(Protocol):
    async def get_all_books(self) -> list[Book]:
        pass


def create_router(book_service: BookService) -> Router:
    router = Router()
    
    @router.callback_query(F.data == KeyboardButton.ShowAllBookList)
    async def process_show_all_book_list(callback: CallbackQuery):
        books = await book_service.get_all_books()
        
        elements = [f"{book.author} — {book.title}" for book in books]
        content = as_list(
            as_marked_section(Bold("Список книг"), *elements, marker="- ")
        )
        await callback.message.edit_text(**content.as_kwargs())
    
    return router