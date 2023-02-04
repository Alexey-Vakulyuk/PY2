class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    # геттеры для атрибутов name и author, которые не позволят их изменять
    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. Бумажная книга """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # наследование значений атрибутов name и author из базового класса
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError(f"Количество страниц должно быть целым числом, а не {type(new_pages)}")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self._pages = new_pages

    def __str__(self) -> str:
        return f"{super().__str__()}. Количество страниц {self.pages}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс книги. Аудио книга """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # наследование значений атрибутов name и author из базового класса
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, (int, float)):
            raise TypeError(f"Продолжительность книги должна быть числом, а не {type(new_duration)}")
        if new_duration <= 0:
            raise ValueError("Продолжительность книги должна быть больше 0")
        self._duration = new_duration

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Продолжительность книги {self.duration}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
