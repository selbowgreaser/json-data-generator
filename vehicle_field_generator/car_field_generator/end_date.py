import random


class EndDateGenerator:
    MINIMUM_SERVICE_LIFE = 1
    MAXIMUM_YEAR = 2030

    def __init__(self,
                 minimum_service_life: int = MINIMUM_SERVICE_LIFE,
                 maximum_year: int = MAXIMUM_YEAR):
        self.minimum_service_life = minimum_service_life
        self.maximum_year = maximum_year

    def generate(self, start_date: str) -> str:
        year = random.randint(self._get_from_year(start_date), self.maximum_year)
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

    def _get_from_year(self, start_date: str):
        return int(start_date[:4]) + self.minimum_service_life


if __name__ == "__main__":
    start_date_generator = EndDateGenerator()
    print(start_date_generator.generate("2012-06-03"))
