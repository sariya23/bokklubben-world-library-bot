from src.domain.book import Book
from typing import Protocol

class BookRepository(Protocol):
    async def get_all_books(self) -> list[Book]:
        pass

class BookService:
    
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo
        
    async def get_all_books(self) -> list[Book]:
        return await self.book_repo.get_all_books()