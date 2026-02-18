from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from src.lexicon.lexicon import LexiconRu
from aiogram.types.link_preview_options import LinkPreviewOptions
from aiogram import Router
from typing import Protocol


def create_router() -> Router:
    router = Router()
    
    @router.message(CommandStart())
    async def process_start_command(message: Message):
        await message.answer(**LexiconRu.StartCommand, link_preview_options=LinkPreviewOptions(is_disabled=True))
        
    @router.message(Command(commands="help"))
    async def process_help_command(message: Message):
        await message.answer(LexiconRu.HelpCommand)
    
    return router
