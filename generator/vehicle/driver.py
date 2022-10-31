import random

from model import Driver
from generator.vehicle.driver_field import *


class DriverGenerator:
    """
    Класс для генерации объекта Driver со случайными значениями полей.

    ...

    Attributes
    ----------
    name_generator : NameGenerator
        генератор имени
    surname_generator : SurnameGenerator
        генератор фамилии
    middle_name_generator : MiddleNameGenerator
        генератор отчества
    age_generator : AgeGenerator
        генератор возраста
    phone_num_generator : PhoneNumberGenerator
        генератор номера телефона

    Methods
    -------
    generate():
        Генерирует объект Driver со случайными значениями полей.
    """

    def __init__(self,
                 name_generator: NameGenerator,
                 surname_generator: SurnameGenerator,
                 middle_name_generator: MiddleNameGenerator,
                 age_generator: AgeGenerator,
                 phone_num_generator: PhoneNumberGenerator
                 ):
        self.age_generator = age_generator
        self.middle_name_generator = middle_name_generator
        self.name_generator = name_generator
        self.phone_num_generator = phone_num_generator
        self.surname_generator = surname_generator

    def generate(self) -> Driver:
        new_driver = Driver(name=self.name_generator.generate(),
                            surname=self.surname_generator.generate(),
                            age=self.age_generator.generate())

        if random.choice((True, False)):
            new_driver.set_middle_name(self.middle_name_generator.generate())

        if random.choice((True, False)):
            new_driver.set_phone_number(self.phone_num_generator.generate())

        return new_driver
