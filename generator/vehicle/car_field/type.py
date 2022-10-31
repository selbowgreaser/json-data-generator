import random

DEFAULT_TYPES = ("Автобус", "Легковой автомобиль", "Грузовой автомобиль")


class TypeGenerator:
    """
    Класс для генерации случайного значения типа транспортного средства.

    ...

    Attributes
    ----------
    available_types : tuple (default = DEFAULT_TYPES)
        коллекция доступных значений типов транспортных средств

    Methods
    -------
    generate():
        Генерирует случайное значение типа транспортного средства.
    """

    def __init__(self,
                 available_types: tuple = DEFAULT_TYPES):
        self.available_types = available_types

    def generate(self) -> str:
        return random.choice(self.available_types)


if __name__ == "__main__":
    type_generator = TypeGenerator()
    print(type_generator.generate())

    type_generator_with_my_types = TypeGenerator(('Вертолет', 'Самолет', 'Самокат'))
    print(type_generator_with_my_types.generate())
