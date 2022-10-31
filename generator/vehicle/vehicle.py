import random

from generator.common import GuidGenerator
from model.vehicle import Vehicle
from generator.vehicle import DriverGenerator
from generator.vehicle.car_field import *


class VehicleGenerator:
    """
    Класс для генерации объекта Vehicle со случайными значениями полей.

    ...

    Attributes
    ----------
    guid_generator : GuidGenerator
       генератор guid
    start_date_generator : StartDateGenerator
       генератор дата начала эксплуатации
    end_date_generator : EndDateGenerator
       генератор дата окончания эксплуатации
    status_generator : StatusGenerator
       генератор статуса
    type_generator : TypeGenerator
       генератор типа транспортного средства
    brand_generator : BrandGenerator
        генератор марки транспортного средства
    driver_generator : DriverGenerator
        генератор объекта Driver

    Methods
    -------
    generate():
       Генерирует объект Vehicle со случайными значениями полей.
    """

    def __init__(self,
                 guid_generator: GuidGenerator,
                 start_date_generator: StartDateGenerator,
                 end_date_generator: EndDateGenerator,
                 status_generator: StatusGenerator,
                 type_generator: TypeGenerator,
                 brand_generator: BrandGenerator,
                 driver_generator: DriverGenerator):
        self.guid_generator = guid_generator
        self.start_date_generator = start_date_generator
        self.brand_generator = brand_generator
        self.end_date_generator = end_date_generator
        self.status_generator = status_generator
        self.type_generator = type_generator
        self.driver_generator = driver_generator

    def generate(self) -> Vehicle:
        new_vehicle = Vehicle(guid=self.guid_generator.generate(),
                              start_date=self.start_date_generator.generate(),
                              brand=self.brand_generator.generate())

        if random.choice((True, False)):
            new_vehicle.set_status(self.status_generator.generate(new_vehicle.end_date))

        if random.choice((True, False)):
            new_vehicle.set_vehicle_type(self.type_generator.generate())

        if random.choice((True, False)):
            new_vehicle.set_end_date(self.end_date_generator.generate(new_vehicle.start_date))

        if random.choice((True, False)):
            new_vehicle.set_driver(self.driver_generator.generate())

        return new_vehicle
