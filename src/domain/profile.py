from dataclasses import dataclass
from collections import UserList
from src.domain.book import Book

@dataclass
class Profile:
    total_readed_books: UserList[Book]
    total_unreaded_books: UserList[Book]