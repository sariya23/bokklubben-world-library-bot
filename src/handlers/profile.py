from aiogram import Router
from aiogram import F
from aiogram.types import CallbackQuery
from src.keyboards.keyboard_profile import keyboard_profile
from src.domain.profile import Profile
from src.lexicon.lexicon import LexiconRu
from src.keyboards.keyboard_profile import KeyboardButtonProfile
from src.keyboards.main_keyboard import KeyboardButton
from typing import Protocol

class ProfileService(Protocol):
    async def get_profile(self, user_id: int) -> Profile:
        pass


def create_router(profile_service: ProfileService) -> Router:
    router = Router()
    
    @router.callback_query(F.data == KeyboardButton.Profile)
    async def process_profile(callback: CallbackQuery):
        profile = await profile_service.get_profile(callback.from_user.id)
        await callback.message.edit_text(**LexiconRu.build_profile_text(
            profile), 
            reply_markup=keyboard_profile.as_markup())
        await callback.answer()
    
    @router.callback_query(F.data == KeyboardButtonProfile.ReadedBooks)
    async def process_readed_books(callback: CallbackQuery):
        profile = await profile_service.get_profile(callback.from_user.id)
        await callback.answer()
    
    @router.callback_query(F.data == KeyboardButtonProfile.UnreadedBooks)
    async def process_unreaded_books(callback: CallbackQuery):
        profile = await profile_service.get_profile(callback.from_user.id)
        await callback.answer()
    
    return router