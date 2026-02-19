from typing import Protocol
from random import choice

from aiogram import Router
from aiogram import F
from aiogram.types import CallbackQuery
from src.keyboards.main_keyboard import KeyboardButton
from src.domain.book import Book
from src.lexicon.lexicon import LexiconRu
from src.domain.profile import Profile

class RandomBookService(Protocol):
    def get_random_book(self) -> Book:
        pass

class ProfileService(Protocol):
    async def get_profile(self, user_id: int) -> Profile:
        pass

def create_router(profile_service: ProfileService) -> Router:
    router = Router()
    
    @router.callback_query(F.data == KeyboardButton.RandomBook)
    async def process_random_book(callback: CallbackQuery):
        profile = await profile_service.get_profile(callback.from_user.id)
        random_book = choice(profile.total_unreaded_books)
        await callback.message.answer(**LexiconRu.build_random_book_text(random_book))
        await callback.answer()
    
    return router