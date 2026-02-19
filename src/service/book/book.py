from src.domain.book import Book
from typing import Protocol
from src.service import error

class BookRepository(Protocol):
    async def get_all_books(self) -> list[Book]:
        pass
    

class BookUserReadedRepository(Protocol):
    async def add_book_user_readed(self, book_id: int, user_id: int):
        pass
    
    async def remove_book_user_readed(self, book_id: int, user_id: int):
        pass
    
    async def get_all_books_user_readed(self, user_id: int) -> list[Book]:
        pass

class BookService:
    
    def __init__(self, book_repo: BookRepository, book_user_readed_repo: BookUserReadedRepository):
        self.book_repo = book_repo
        self.book_user_readed_repo = book_user_readed_repo
        
    async def get_all_books(self) -> list[Book]:
        return await self.book_repo.get_all_books()
    
    async def mark_readed_book(self, book_id: int, user_id: int):
        try:
            await self.book_user_readed_repo.add_book_user_readed(book_id, user_id)
        except error.UserAlredyReadedBookError:
            await self.book_user_readed_repo.remove_book_user_readed(book_id, user_id)