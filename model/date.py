class Date:
    def __init__(self,
                 year: int,
                 month: int,
                 day: int):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self) -> str:
        return f'{self.year}-{self.month:02}-{self.day:02}'
