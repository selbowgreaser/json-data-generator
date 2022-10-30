import random


class AgeGenerator:
    def __init__(self,
                 minimum_age: int = 18,
                 maximum_age: int = 99):
        self.minimum_age = minimum_age
        self.maximum_age = maximum_age

    def generate(self) -> int:
        return random.randint(self.minimum_age, self.maximum_age)


if __name__ == "__main__":
    age_generator = AgeGenerator()
    print(age_generator.generate())

    age_generator_with_changed_minimum_age = AgeGenerator(minimum_age=50)
    print(age_generator_with_changed_minimum_age.generate())
