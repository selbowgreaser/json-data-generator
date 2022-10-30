import random


class StartDateGenerator:
    def __init__(self,
                 start_year: int = 2000,
                 end_year: int = 2022):
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
