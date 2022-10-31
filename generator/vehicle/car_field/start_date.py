import random

END_YEAR = 2022
START_YEAR = 2000


class StartDateGenerator:
    """
    Класс для генерации случайного значения даты начала эксплуатации транспортного средства.

    ...

    Attributes
    ----------
    start_year : int (default = START_YEAR)
        минимально возможный год для генерации
    end_year : int (default = END_YEAR)
        максимально возможный год для генерации

    Methods
    -------
    generate():
        Генерирует случайное значение даты начала эксплуатации транспортного средства.
    """

    def __init__(self,
                 start_year: int = START_YEAR,
                 end_year: int = END_YEAR):
        self.start_year = start_year
        self.end_year = end_year

    def generate(self) -> str:
        year = random.randint(self.start_year, self.end_year)
        month = random.randint(1, 12)
        if month in (1, 3, 5, 7, 8, 10, 12):
            day = random.randint(1, 31)
        elif month in (4, 6, 9, 11):
            day = random.randint(1, 30)
        else:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                day = random.randint(1, 29)
            else:
                day = random.randint(1, 28)
        return f'{year}-{month:02}-{day:02}'


if __name__ == "__main__":
    start_date_generator = StartDateGenerator()
    print(start_date_generator.generate())

    start_date_generator_with_not_default_period = StartDateGenerator(1230, 1360)
    print(start_date_generator_with_not_default_period.generate())
