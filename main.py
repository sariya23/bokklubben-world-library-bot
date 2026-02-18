from src.config.config import create_config
from src.parse_args import parse_args
from src.handlers import user, other
from aiogram import Bot, Dispatcher
from src.service.book.book import BookService

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
    
    user_router = user.create_router()
    other_router = other.create_router()
    disp.include_router(user_router)
    disp.include_router(other_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await disp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())