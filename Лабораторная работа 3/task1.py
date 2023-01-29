class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    # геттеры для атрибутов name и author, которые не позволят их изменять
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. Бумажная книга """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # наследование значений атрибутов name и author из базового класса
        # проверка на тип данных и значение атрибута pages, и присвоение ему значения
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise ValueError("Количество страниц должно быть больше 0")
        else:
            raise TypeError(f"Количество страниц должно быть целым числом, а не {type(pages)}")

    def __str__(self) -> str:
        return f"{super().__str__()}. Количество страниц {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс книги. Аудио книга """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # наследование значений атрибутов name и author из базового класса
        # проверка на тип данных и значение атрибута duration, и присвоение ему значения
        if isinstance(duration, (float, int)):
            if duration > 0:
                self.duration = duration
            else:
                raise ValueError("Продолжительность книги должна быть больше 0")
        else:
            raise TypeError(f"Продолжительность книги должна быть числом с плавающей запятой, а не {type(duration)}")

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Продолжительность книги {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
