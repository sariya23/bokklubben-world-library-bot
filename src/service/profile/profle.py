from typing import Protocol
from src.domain.book import BookList
from src.domain.profile import Profile


class BookRepository(Protocol):
    async def get_all_books(self) -> BookList:
        pass
    

class BookUserReadedRepository(Protocol):    
    async def get_all_books_user_readed(self, user_id: int) -> BookList:
        pass

class ProfileService:
    def __init__(self, book_repo: BookRepository, book_user_readed_repo: BookUserReadedRepository):
        self.book_repo = book_repo
        self.book_user_readed_repo = book_user_readed_repo
    
    async def get_profile(self, user_id: int) -> Profile:
        total_books = await self.book_repo.get_all_books()
        total_readed_books = await self.book_user_readed_repo.get_all_books_user_readed(user_id)
        total_unreaded_books = BookList(b for b in total_books if b not in total_readed_books)
        return Profile(total_readed_books, total_unreaded_books)