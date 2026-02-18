from src.keyboards.keyboard import KeyboardButtonBase
from src.lexicon.lexicon import LexiconRu
from aiogram.types.link_preview_options import LinkPreviewOptions
from src.keyboards.main_keyboard import keyboard_main
from aiogram import Router
from aiogram import F
from aiogram.types import CallbackQuery



def create_router() -> Router:
    router = Router()
    
    @router.callback_query(F.data == KeyboardButtonBase.ToMenu)
    async def process_to_menu(callback: CallbackQuery):
        await callback.message.edit_text(**LexiconRu.StartCommand, link_preview_options=LinkPreviewOptions(is_disabled=True), reply_markup=keyboard_main)
    
        
    @router.callback_query(F.data == KeyboardButtonBase.Stub)
    async def process_stub(callback: CallbackQuery):
        await callback.answer()
    
    return router