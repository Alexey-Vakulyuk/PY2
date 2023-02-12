import doctest
from typing import Dict


class Cat:
    def __init__(self, name: str, gender: str, age: int, city: str):

        """
                Создание и подготовка к работе объекта "Кот"
                :param name: Кличка животного
                :param gender: Пол животного
                :param age: Возраст животного (полных лет)
                :raises TypeError: Атрибут name должен быть str
                :raises ValueError: Атрибут gender может принимать только значения m и f
                :raises TypeError: Атрибут gender должен быть str
                :raises ValueError: Атрибут age должен быть больше нуля
                :raises TypeError: Атрибут age должен быть int

                >>> the_cat = Cat('Мурка', 'f', 7, 'Санкт-Петербург')
        """
        if not isinstance(name, str):
            raise TypeError(f'имя животного должно быть строкой, а не {type(name)}')
        self.name = name

        if not isinstance(gender, str):
            raise TypeError(f'пол животного должен быть строкой, а не {type(gender)}')
        if (gender != 'm') and (gender != 'f'):
            raise ValueError('пол животного может принимать 2 значения: m — кот; f — кошка')
        self.gender = gender

        if not isinstance(age, int):
            raise TypeError(f'возраст животного должен быть целым числом, а не {type(age)}')
        if age < 0:
            raise ValueError('возраст животного должен быть положительным числом')
        self.age = age

        if not isinstance(city, str):
            raise TypeError(f'название города должно быть строкой, а не {type(city)}')
        self.city = city

    def __str__(self) -> str:
        """
        Магический метод для отображения информации об объекте класса для пользователей
        :return: Строка, показывающая содержание класса пользователю
        Примеры:
        >>> Cat('Мурка', 'f', 7, 'Санкт-Петербург').__str__()
        'Кошка Мурка, Возраст: 7, Город: Санкт-Петербург'
        """
        if self.gender == 'm':
            return f"Кот {self.name}, Возраст: {self.age}, Город: {self.city}"
        elif self.gender == 'f':
            return f"Кошка {self.name}, Возраст: {self.age}, Город: {self.city}"

    def __repr__(self) -> str:
        """
        Магический метод для отображения информации об объекте класса
        :return: Строка, показывающая, как может быть инициализирован экземпляр класса
        Примеры:
        >>> Cat('Мурка', 'f', 7, 'Санкт-Петербург').__repr__()
        "Cat(name='Мурка', gender='f', age=7, city=Санкт-Петербург)"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, gender={self.gender!r}, " \
               f"age={self.age!r}, city={self.city})"

    def pet_the_cat(self) -> None:
        """
        Метод, позволяющий погладить кота
        Примеры:
        >>> Cat('Мурка', 'f', 7, 'Санкт-Петербург').pet_the_cat()
        """
        ...

    def is_boarding_suitable(self, boarding: Dict[str, float], minimum_rating: float) -> bool:
        """
                Метод, позволяющий определить подходит ли передержка для кота по городу и рейтингу
                :param boarding: Словарь, описывающий передержку; первый ключ — 'город',
                значение — строка название города; второй ключ — 'оценка сервиса', значение — оценка от 0 до 5
                :param minimum_rating: Минимальный допустимый рейтинг передержки
                :raise TypeError: Аргумент boarding должен быть словарем
                :raise TypeError: Значение boarding['город'] должно быть строкой
                :raise TypeError: Значение boarding['оценка сервиса'] должно быть числом
                :raise ValueError: Значение boarding['оценка сервиса'] должен быть числом от 0 до 5
                :raise TypeError: Аргумент minimum_rating должен быть числом
                :raise ValueError: Аргумент minimum_rating должен быть числом от 0 до 5
                Примеры:
                >>> Cat('Мурка', 'f', 7, 'Санкт-Петербург').is_boarding_suitable({'город': 'Санкт-Петербург', 'оценка сервиса': 4}, 3.5)
                True
        """
        if not isinstance(boarding, dict):
            raise TypeError(f'информация о передержке должна быть представлена в виде словаря, а не быть {type(boarding)}')
        if not isinstance(boarding['город'], str):
            raise TypeError(f'название города должно быть строкой, а не {type(boarding["город"])}')
        if not isinstance(boarding['оценка сервиса'], (int, float)):
            raise TypeError(f'рейтинг должен быть числом, а не {type(boarding["оценка сервиса"])}')
        if not (0 <= boarding["оценка сервиса"] <= 5):
            raise ValueError('рейтинг должен быть числом от 0 до 5')

        if not isinstance(minimum_rating, (int, float)):
            raise TypeError(f'минимальный допустимый рейтинг должен быть числом, а не {type(minimum_rating)}')
        if not (0 <= minimum_rating <= 5):
            raise ValueError('минимальный допустимый рейтинг должен быть числом от 0 до 5')

        if self.city == boarding['город']:  # подходит ли город
            if boarding['оценка сервиса'] >= minimum_rating:    # подходит ли передержка по рейтингу
                return True
            else:
                return False
        else:
            return False


class ExoticShorthair(Cat):
    def __init__(self, name: str, gender: str, age: int, city: str, color: tuple, furs_length: str):

        """
                Создание и подготовка к работе объекта "Экзотическая короткошёрстная кошка"
                :param name: Кличка животного
                :param gender: Пол животного
                :param age: Возраст животного
                :param color: Кортеж, в котором перечисляются все цвета в окраске животного
                :param furs_length: Длина шерсти животного
                :raises TypeError: Атрибут name должен быть str
                :raises ValueError: Атрибут gender может принимать только значения m и f
                :raises TypeError: Атрибут gender должен быть str
                :raises ValueError: Атрибут age должен быть больше нуля
                :raises TypeError: Атрибут age должен быть int
                :raises TypeError: Атрибут color должен быть tuple
                :raises TypeError: Атрибут furs_length должен быть int

                >>> the_exotic_shorthair = ExoticShorthair('Барсик', 'm', 5, 'Санкт-Петербург', ('черный', 'белый'), 'короткая')
        """

        super().__init__(name, gender, age, city)

        if not isinstance(color, tuple):
            raise TypeError(f'цвет животного должен быть кортежем, а не {type(color)}')
        self.color = color

        if furs_length is None:
            furs_length = 'короткая'  # значение по умолчанию
        if not isinstance(furs_length, str):
            raise TypeError(f'длина шерсти животного должна быть строкой, а не {type(furs_length)}')
        self.furs_length = furs_length

    def __str__(self) -> str:
        """
        Магический метод для отображения информации об объекте класса для пользователей
        :return: Строка, показывающая содержание класса пользователю
        Примеры:
        >>> ExoticShorthair('Барсик', 'm', 5, 'Санкт-Петербург', ('черный', 'белый'), 'короткая').__str__()
        "Кот Барсик, Возраст: 5, Город: Санкт-Петербург, Цвет: ('черный', 'белый'), Длина шерсти: короткая"
        """
        return f"{super().__str__()}, Цвет: {self.color}, Длина шерсти: {self.furs_length}"

    def __repr__(self) -> str:
        """
        Магический метод для отображения информации об объекте класса
        :return: Строка, показывающая, как может быть инициализирован экземпляр класса
        Примеры:
        >>> ExoticShorthair('Барсик', 'm', 5, 'Санкт-Петербург', ('черный', 'белый'), 'короткая').__repr__()
        "ExoticShorthair(name='Барсик', gender='m', age=5, city=Санкт-Петербург, color=('черный', 'белый'), furs_length=короткая)"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, gender={self.gender!r}, age={self.age!r}," \
               f" city=Санкт-Петербург, color={self.color!r}, furs_length={self.furs_length})"

    def is_boarding_suitable(self, boarding: Dict[str, float], minimum_rating: float, is_familiar: bool) -> bool:
        """
                Метод, позволяющий определить подходит ли передержка для кота. Перегружен так как экзотическая
                короткошерстная кошка очень настороженно относятся к незнакомцам, поэтому не стоит отдавать кошку
                на передержку к чужим для нее людям. По этой причине добавлен отбор по факту знакомства животного с
                людьми из передержки
                :param boarding: Словарь, описывающий передержку; первый ключ — 'город',
                значение — строка название города; второй ключ — 'оценка сервиса', значение — оценка от 0 до 5
                :param minimum_rating: Минимальный допустимый рейтинг передержки
                :param is_familiar: Знакомо ли животное с людьми из передержки; если да — True, если нет — False
                :raise TypeError: Аргумент boarding должен быть словарем
                :raise TypeError: Значение boarding['город'] должно быть строкой
                :raise TypeError: Значение boarding['оценка сервиса'] должно быть числом
                :raise ValueError: Значение boarding['оценка сервиса'] должен быть числом от 0 до 5
                :raise TypeError: Аргумент minimum_rating должен быть числом
                :raise ValueError: Аргумент minimum_rating должен быть числом от 0 до 5
                :raise TypeError: Аргумент is_familiar должно быть типа bool
                Примеры:
                >>> ExoticShorthair('Барсик', 'm', 5, 'Санкт-Петербург', ('черный', 'белый'), 'короткая').is_boarding_suitable({'город': 'Санкт-Петербург', 'оценка сервиса': 4}, 3.5, True)
                True
        """

        if not isinstance(is_familiar, bool):
            raise TypeError(f'факт знакомства животного с передержкой должно быть выражено логическим типом, а не {type(is_familiar)}')

        super().is_boarding_suitable(boarding, minimum_rating)

        if is_familiar:
            return True
        else:
            return False


if __name__ == "__main__":
    doctest.testmod()
    pass
