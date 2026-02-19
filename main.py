from src.config.config import create_config
from src.parse_args import parse_args
from src.handlers import user, other, base
from aiogram import Bot, Dispatcher
from src.keyboards.menu_commands import set_main_menu
from src.handlers import book
from src.service.book.book import BookService
from src.infra.postrgres.postgres import Postgres

import logging
import asyncio

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    args = parse_args()
    config = create_config(args.env_path)
    logging.info("config load successfully")
    logging.info(f"env type: {config.env_type.env_type}")
    
    bot = Bot(token=config.bot.bot_token)
    disp = Dispatcher()
    db = Postgres(config.db)
    
    book_service = BookService(db, db)
    user_router = user.create_router()
    other_router = other.create_router()
    book_router = book.create_router(book_service)
    base_router = base.create_router()
    
    await set_main_menu(bot)
    
    disp.include_router(user_router)
    disp.include_router(other_router)
    disp.include_router(book_router)
    disp.include_router(base_router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await disp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())