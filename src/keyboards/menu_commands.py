from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats

from src.lexicon.lexicon import LexiconCommands


async def set_main_menu(bot: Bot):
    """Функция для настройки кнопки Menu бота"""
    main_menu_commands = [
        BotCommand(command=command.command, description=command.description)
        for command in LexiconCommands().get_commands()
    ]
    await bot.set_my_commands(
        commands=main_menu_commands,
        scope=BotCommandScopeAllPrivateChats()
    )