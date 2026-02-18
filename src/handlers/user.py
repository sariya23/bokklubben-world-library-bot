from aiogram.types import Message
from aiogram.filters import CommandStart
from src.lexicon.lexicon import LexiconRu
from aiogram import Router

router = Router()
    
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(**LexiconRu.StartCommand.as_kwargs())