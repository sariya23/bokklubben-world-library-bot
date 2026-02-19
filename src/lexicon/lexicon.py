from aiogram.utils.formatting import Bold, Text, TextLink
from dataclasses import dataclass
from typing import Any
from src.domain.profile import Profile
from aiogram.utils.formatting import as_list
from src.domain.book import Book
class LexiconRu:
    StartCommand = Text("Привет! 👋",
                        "\n", "\n",
                        "Это бот поможешь читать книги из списка Норвежского клуба и следить за своим прогрессом чтения.",
                        "\n", "\n",
                        "Здесь ты можешь:",
                        "\n",
                        "📚 посмотреть какие книги есть в списке",
                        "\n",
                        "✅ отмечать прочитанные и выбирать следующую случайно",
                        "\n",
                        "📊 отслеживать свой прогресс",
                        "\n", "\n",
                        "Начни с выбора книги или отметь уже прочитанные.",
                        "\n", "\n",
                        "👇 Выбери действие:").as_kwargs()
    HelpCommand = """Если хочешь вернуться в главное меню, отправь команду /start.
Полный список команд можно открыть через кнопку Меню слева от поля ввода."""
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
        read_count = len(profile.total_readed_books)
        unread_count = len(profile.total_unreaded_books)
        total = read_count + unread_count
        percent = int((read_count / total * 100)) if total else 0
        bar_length = 20
        filled = round(percent / 100 * bar_length)
        progress_bar = "█" * filled + "░" * (bar_length - filled)
        return Text("👤 ",
                    Bold("Твой профиль"),
                    "\n", "\n",
                    f"📚 Прочитано: {read_count}",
                    "\n",
                    f"📖 Осталось: {unread_count}",
                    "\n",
                    f"📊 Прогресс: {percent}%",
                    "\n", "\n",
                    progress_bar,
                    " ",
                    f"{percent}%",
                    "\n", "\n",
                    "Продолжай читать - ты на отличном пути 🚀").as_kwargs()
        
    @staticmethod
    def build_random_book_text(book: Book) -> dict[str, Any]:
        return Text("📚 ",
                    Bold("Не знаешь, что читать дальше?"),
                    "\n", "\n",
                    "Попробуй эту книгу:",
                    "\n", "\n",
                    f"«{book.title}» — {book.author}",
                    "\n", "\n",
                    "Она может тебя удивить 😉").as_kwargs()

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