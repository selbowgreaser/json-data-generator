import random

DEFAULT_SURNAMES = (
    "Иванов", "Смирнов", "Кузнецов", "Попов", "Васильев", "Петров", "Соколов", "Михайлов", "Новиков", "Фёдоров",
    "Морозов", "Волков", "Алексеев", "Лебедев", "Семёнов", "Егоров", "Павлов", "Козлов", "Степанов", "Николаев",
    "Орлов", "Андреев", "Макаров", "Никитин", "Захаров")


class SurnameGenerator:
    def __init__(self,
                 available_surnames: tuple = DEFAULT_SURNAMES):
        self.available_surnames = available_surnames

    def generate(self) -> str:
        return random.choice(self.available_surnames)


if __name__ == "__main__":
    surname_generator = SurnameGenerator()
    print(surname_generator.generate())

    surname_generator_with_my_surnames = SurnameGenerator(('Стейтем', 'Шварцнеггер', 'Сталоне'))
    print(surname_generator_with_my_surnames.generate())
