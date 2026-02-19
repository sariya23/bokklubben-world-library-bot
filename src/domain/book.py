from dataclasses import dataclass
from collections import UserList

@dataclass
class Book:
    id: int
    title: str
    author: str
    country: str
    century: int
    
class BookList(UserList):
    @property
    def book_ids(self) -> list[int]:
        return [book.id for book in self]