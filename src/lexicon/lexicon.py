from aiogram.utils.formatting import Bold, Text, TextLink
from dataclasses import dataclass
from typing import Any
from src.domain.profile import Profile
from src.domain.book import Book
class LexiconRu:
    StartCommand = Text("📚",
                        Bold('Всемирная библиотека'),
                        "\n", "\n",
                        "Этот бот поможет прочитать книги из ", 
                        TextLink("Всемирной библиотеки ", url="https://knigi.fandom.com/ru/wiki/%D0%92%D1%81%D0%B5%D0%BC%D0%B8%D1%80%D0%BD%D0%B0%D1%8F_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0_(%D0%9D%D0%BE%D1%80%D0%B2%D0%B5%D0%B6%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%BD%D0%B8%D0%B6%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BB%D1%83%D0%B1)"), 
                        "и ничего не упустить",
                        "\n", "\n",
                        "Для просмотра списка доступных команд используйте команду /help").as_kwargs()
    HelpCommand = """Для повторного вызова начального сообщения используйте команду /start. Для просмотра всего списка команд
используйте кнопку Меню слева от поля ввода сообщения"""
    UnknownCommand = Text("❌", Bold("Я не знаю такой команды")).as_kwargs()
    InternalError = Text("❌", Bold("Внутренняя ошибка")).as_kwargs()
    BackPagination = "⏪"
    ForwardPagination = "⏩"
    BookMarkedAsReaded = "✅"
    ToMenuButton = "📖 В меню"
    MarkAlreadyReaded = Text("📚",
                        Bold("Отметить прочитанные книги"),
                        "\n", "\n",
                        "Выберите книгу, чтобы отметить ее как прочитанную",
                        "\n", "\n",
                        "Прочитанные книги будут исключены из случайного выбора. Чтобы вернуть книгу в пул нажмите на соответсвующую кнопку еще раз").as_kwargs()
    
    @staticmethod
    def build_profile_text(profile: Profile) -> dict[str, Any]:
        return Text("📊",
                    Bold("Профиль"),
                    "\n", "\n",
                    f"Прочитано: {len(profile.total_readed_books)}",
                    "\n",
                    f"Осталость прочитать: {len(profile.total_unreaded_books)}",
                    "\n",
                    f"Процент завершения: {int((len(profile.total_readed_books) / len(profile.total_unreaded_books)) * 100)}%").as_kwargs()
        
    @staticmethod
    def build_random_book_text(book: Book) -> dict[str, Any]:
        return Text("🎲",
                    Bold("Случайная книга"),
                    "\n", "\n",
                    f"Книга: {book.title}",
                    "\n",
                    f"Автор: {book.author}").as_kwargs()

@dataclass
class Command:
    command: str
    description: str

class LexiconCommands:
    StartCommand = Command("/start", "Начать работу с ботом")
    HelpCommand = Command("/help", "Если непонятно что делать")
    __commands = [StartCommand, HelpCommand]
    
    def get_commands(self) -> list[Command]:
        return self.__commands