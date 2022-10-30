import random


class AgeGenerator:
    def __init__(self,
                 minimum_age: int = 18,
                 maximum_age: int = 70,
                 mu: int = 35,
                 sigma: int = 12):
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
