from src.domain.book import Book

class BookService:
    async def get_all_books(self) -> list[Book]:
        return [Book(id=1, title="asd", author="qwe") for _ in range(100)]