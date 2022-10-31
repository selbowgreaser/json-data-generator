import random

MINIMUM_SERVICE_LIFE = 1
MAXIMUM_SERVICE_LIFE = 10


class EndDateGenerator:
    """
    Класс для генерации случайного значения даты окончания эксплуатации транспортного средства.

    ...

    Attributes
    ----------
    minimum_service_life : int (default = MINIMUM_SERVICE_LIFE)
        минимально возможный срок эксплуатации транспортного средства (при значении 0 могут возникать логические ошибки)
    maximum_service_life : int (default = MAXIMUM_SERVICE_LIFE)
        максимально возможный срок эксплуатации транспортного средства

    Methods
    -------
    generate():
        Генерирует случайное значение даты окончания эксплуатации транспортного средства.
    """

    def __init__(self,
                 minimum_service_life: int = MINIMUM_SERVICE_LIFE,
                 maximum_service_life: int = MAXIMUM_SERVICE_LIFE):
        self.minimum_service_life = minimum_service_life
        self.maximum_service_life = maximum_service_life

    def generate(self, start_date: str) -> str:
        year = random.randint(self._get_from_year(start_date), self._get_to_year(start_date))
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

    def _get_to_year(self, start_date: str):
        return int(start_date[:4]) + self.minimum_service_life + self.maximum_service_life


if __name__ == "__main__":
    start_date_generator = EndDateGenerator()
    print(start_date_generator.generate("2012-06-03"))
