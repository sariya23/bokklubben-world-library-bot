from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    author: str
    country: str
    century: int