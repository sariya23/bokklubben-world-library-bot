from aiogram.utils.formatting import Bold, Text

class LexiconRu:
    StartCommand = Text("📚", Bold('Всемирная библиотека'))
    UnknownCommand = Text("❌", Bold('Я не знаю такой команды'))
    InternalError = Text("❌", Bold('Внутренняя ошибка'))