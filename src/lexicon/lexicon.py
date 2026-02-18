from aiogram.utils.formatting import Bold, Text, TextLink, as_list, as_marked_section

class LexiconRu:
    StartCommand = Text("📚",
                        Bold('Всемирная библиотека'),
                        "\n", "\n",
                        "Этот бот поможет прочитать книги из ", 
                        TextLink("Всемирной библиотеки ", url="https://knigi.fandom.com/ru/wiki/%D0%92%D1%81%D0%B5%D0%BC%D0%B8%D1%80%D0%BD%D0%B0%D1%8F_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0_(%D0%9D%D0%BE%D1%80%D0%B2%D0%B5%D0%B6%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%BD%D0%B8%D0%B6%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BB%D1%83%D0%B1)"), 
                        "и ничего не упустить",
                        "\n", "\n",
                        "Для просмотра списка доступных команд используйте команду /help").as_kwargs()
    HelpCommand = as_list(as_marked_section(
        Bold("Доступные команды:\n"),
        "/start - Начать работу с ботом"
        "/help - Посмотреть список доступных команд",
        marker="⚒️"
    )).as_kwargs()
    UnknownCommand = Text("❌", Bold('Я не знаю такой команды')).as_kwargs()
    InternalError = Text("❌", Bold('Внутренняя ошибка')).as_kwargs()