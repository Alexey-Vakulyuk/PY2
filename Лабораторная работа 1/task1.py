import doctest
from typing import Tuple, Dict


class Door:
    def __init__(self, material: str, color: str, width_height: Tuple[float, float]):
        """
                Создание и подготовка к работе объекта "Дверь"
                :param material: Материал двери
                :param color: Цвет двери
                :param width_height: Ширина и высота двери в сантиметрах
                Примеры:
                >>> the_door = Door('дерево', 'черный', (90, 200))  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError(f'название материала должно быть строкой, а не {type(material)}')
        self.material = material

        if not isinstance(color, str):
            raise TypeError(f'название цвета должно быть строкой, а не {type(color)}')
        self.color = color

        if not isinstance(width_height, tuple):
            raise TypeError(f'ширина и высота должны быть записаны в кортеже, а не быть {type(width_height)}')
        if (not isinstance(width_height[0], (float, int))) or (not isinstance(width_height[1], (float, int))):
            raise TypeError(f'ширина и высота должны быть числом, а не {type(width_height[0])}'
                            f' и {type(width_height[1])}')
        if (width_height[0] <= 0) or (width_height[1] <= 0):
            raise ValueError('ширина и высота должны быть больше нуля')
        self.width_height = width_height

    def is_door_closed(self) -> bool:
        """
        Функция, которая проверяет закрыта ли дверь
        :return: Закрыта ли дверь
        Примеры:
        >>> the_door = Door('дерево', 'черный', (90, 200))
        >>> the_door.is_door_closed()
        """
        ...

    def change_door_state(self) -> None:
        """
        Изменение состояния двери (из закрытой в открытую или наоборот)
        Примеры:
        >>> the_door = Door('дерево', 'черный', (90, 200))
        >>> the_door.change_door_state()
        """
        ...


class University:
    def __init__(self, students_number: int, ranking_place: int, rectors_surname: str):
        """
                Создание и подготовка к работе объекта "Университет"
                :param students_number: Количество студентов в университете
                :param ranking_place: Место университета в рейтинге
                :param rectors_surname: Фамилия ректора университета
                Примеры:
                >>> university = University(31537, 257, 'Садов')  # инициализация экземпляра класса
        """
        if not isinstance(students_number, int):
            raise TypeError(f'количество студентов должно быть целым числом, а не {type(students_number)}')
        self.students_number = students_number

        if not isinstance(ranking_place, int):
            raise TypeError(f'место университета в рейтинге должно быть целым числом, а не {type(ranking_place)}')
        self.ranking_place = ranking_place

        if not isinstance(rectors_surname, str):
            raise TypeError(f'фамилия ректора должна быть строкой, а не {type(rectors_surname)}')
        self.rectors_surname = rectors_surname

    def change_ranking_place(self, delta_ranking_place: int) -> None:
        """
        Смена места университета в рейтинге.
        :param delta_ranking_place: Изменение места университета в рейтинге
        :raise TypeError: Если разница между начальным и конечным положением университета в рейтинге не целое число,
         то возвращается ошибка.
        :raise ValueError: Если конечное место в рейтинге меньше 1, то возвращается ошибка.
        Примеры:
        >>> university = University(31537, 257, 'Садов')
        >>> university.change_ranking_place(-5)
        """
        if not isinstance(delta_ranking_place, int):
            raise TypeError(f'разница между начальным и конечным положением университета в рейтинге должна быть целым '
                            f'числом, а не {type(delta_ranking_place)}')
        ...

    def change_rector(self, new_rector_surname: str) -> None:
        """
        Смена ректора.
        :param new_rector_surname: Фамилия нового ректора
        :raise TypeError: Если фамилия ректора не строка, то возвращается ошибка.
        Примеры:
        >>> university = University(31537, 257, 'Садов')
        >>> university.change_rector('Граблин')
        """
        if not isinstance(new_rector_surname, str):
            raise TypeError(f'фамилия нового ректора должна быть строкой, а не {type(new_rector_surname)}')


class Zoo:
    def __init__(self, animals: Dict[str, int], city: str):
        """
                Создание и подготовка к работе объекта "Зоопарк"
                :param animals: Словарь, в котором ключ это вид животных, а значение это их количество
                :param city: Название города
                Примеры:
                >>> zoo = Zoo({'Procyon lotor': 4, 'Canis lupus': 7}, 'Москва')  # инициализация экземпляра класса
        """
        if not isinstance(animals, dict):
            raise TypeError(f'информация о животных должная быть записана в словаре, а не в {type(animals)}')
        self.animals = animals

        if not isinstance(city, str):
            raise TypeError(f'название города должно быть строкой, а не {type(city)}')
        self.city = city

    def add_new_animal(self, new_animal_name: str, new_animal_number: int) -> None:
        """
        Добавление новых животных в зоопарк.
        :param new_animal_name: Вид нового животного
        :param new_animal_number: Количество новых животных
        :raise ValueError: Если количество новых животных меньше нуля, то возвращается ошибка.
        :raise TypeError: Если количество новых животных не целое число, то возвращается ошибка.
        :raise TypeError: Если кназвание нового животного не строка, то возвращается ошибка.
        Примеры:
        >>> zoo = Zoo({'Procyon lotor': 4, 'Canis lupus': 7}, 'Москва')
        >>> zoo.add_new_animal('Ceratotherium simum', 1)
        """
        if not isinstance(new_animal_name, str):
            raise TypeError(f'название нового животного должно быть строкой, а не {type(new_animal_name)}')

        if not isinstance(new_animal_number, int):
            raise TypeError(f'количество новых животных должно быть целым числом, а не {type(new_animal_number)}')
        if new_animal_number <= 0:
            raise ValueError('количество новых животных должно быть больше нуля')

        ...

    def change_animals_number(self, animal_name: str, delta_number: int):
        """
        Смена числа имеющихся в зоопарке животных.
        :param animal_name: Вид животного
        :param delta_number: Изменение количества животных
        :raise TypeError: Если изменение количества животных не целое число, то возвращается ошибка.
        :raise TypeError: Если название животного не строка, то возвращается ошибка.
        Примеры:
        >>> zoo = Zoo({'Procyon lotor': 4, 'Canis lupus': 7}, 'Москва')
        >>> zoo.change_animals_number('Canis lupus', -2)
        """
        if not isinstance(animal_name, str):
            raise TypeError(f'название животного должно быть строкой, а не {type(animal_name)}')

        if not isinstance(delta_number, int):
            raise TypeError(f'изменение количества животных должно быть целым числом, а не {type(animal_name)}')

        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
