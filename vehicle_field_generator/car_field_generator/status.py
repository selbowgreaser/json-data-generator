import datetime
import random

TODAY = str(datetime.date.today())
DEFAULT_ACTIVE_STATUSES = ("В ремонте", "Активный", "Снят с эксплуатации")
DEFAULT_OFF_STATUSES = ("Снят с эксплуатации",)


class StatusGenerator:
    def __init__(self,
                 available_active_statuses: tuple = DEFAULT_ACTIVE_STATUSES,
                 available_off_statuses: tuple = DEFAULT_OFF_STATUSES):
        self.available_active_statuses = available_active_statuses
        self.available_off_statuses = available_off_statuses
        self.available_all_statuses = available_active_statuses + available_off_statuses

    def generate(self, end_date) -> str:
        if end_date:
            if end_date < TODAY:
                return random.choice(self.available_off_statuses)
            else:
                return random.choice(self.available_active_statuses)
        else:
            return random.choice(self.available_all_statuses)


if __name__ == "__main__":
    status_generator = StatusGenerator()
    print(status_generator.generate("2022-09-15"))

    status_generator_with_my_statuses = StatusGenerator(('Работаю', 'Играю'), ('Отдыхаю',))
    print(status_generator_with_my_statuses.generate("2025-10-16"))
