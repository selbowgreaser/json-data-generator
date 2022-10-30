import random

DEFAULT_TYPES = ("Автобус", "Легковой автомобиль", "Грузовой автомобиль")


class TypeGenerator:
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
