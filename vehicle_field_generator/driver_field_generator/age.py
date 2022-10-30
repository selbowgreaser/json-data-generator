import random

MINIMUM_AGE = 18
MAXIMUM_AGE = 70
MU = 35
SIGMA = 12


class AgeGenerator:
    """
    Класс для генерации случайного значения возраста водителя.

    ...

    Attributes
    ----------
    minimum_age : tuple (default = MINIMUM_AGE)
        минимальный возраст для водителя
    maximum_age : tuple (default = MAXIMUM_AGE)
        максимальный возраст для водителя
    mu : tuple (default = MU)
        математическое ожидание возраста водителя
    sigma : tuple (default = SIGMA)
        стандартное отклонение возраста водителя

    Methods
    -------
    generate():
        Генерирует случайное значение возраста водителя.
    """

    def __init__(self,
                 minimum_age: int = MINIMUM_AGE,
                 maximum_age: int = MAXIMUM_AGE,
                 mu: int = MU,
                 sigma: int = SIGMA):
        self.minimum_age = minimum_age
        self.maximum_age = maximum_age
        self.mu = mu
        self.sigma = sigma

    def generate(self) -> int:
        age = round(random.normalvariate(self.mu, self.sigma))
        while not self.minimum_age <= age <= self.maximum_age:
            age = round(random.normalvariate(self.mu, self.sigma))
        return age


if __name__ == "__main__":
    age_generator = AgeGenerator()
    print(age_generator.generate())

    age_generator_with_changed_minimum_age = AgeGenerator(minimum_age=50)
    print(age_generator_with_changed_minimum_age.generate())
