from aiogram.types import Message
from aiogram.filters import CommandStart
from src.lexicon.lexicon import LexiconRu
from aiogram.types.link_preview_options import LinkPreviewOptions
from aiogram import Router

router = Router()
    
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(**LexiconRu.StartCommand, link_preview_options=LinkPreviewOptions(is_disabled=True))