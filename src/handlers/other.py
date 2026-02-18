from aiogram.types import Message
from aiogram import Router

from src.lexicon.lexicon import LexiconRu

def create_router() -> Router:
    router = Router()
    
    @router.message()
    async def send_echo(message: Message):
        try:
            await message.answer(**LexiconRu.UnknownCommand)
        except TypeError:
            await message.answer(**LexiconRu.InternalError)
    
    return router