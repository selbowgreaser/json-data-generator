import json

from generator.common.guid import *
from generator.vehicle import *
from generator.vehicle.car_field import *
from generator.vehicle.driver_field import *

NUMBER_OF_OBJECTS = 10
NUMBER_OF_OBJECTS_PER_FILE = 10
PATH = r""


class JsonCreator:
    """
    Класс для создания JSON файлов.

    ...

    Attributes
    ----------
    vehicle_generator : VehicleGenerator
        генератор объектов транспортных средств
    number_of_objects : int (default = NUMBER_OF_OBJECTS)
        количество генерируемых объектов
    number_of_objects_per_file : int (default = NUMBER_OF_OBJECTS_PER_FILE)
        количество объектов, сохраненных в одном файле
    path : str (default = PATH)
        путь до папки, в которой будет лежать json файл(-ы)
    include_none : bool (default = False)
        флаг, который отвечает за включение полей со значением null в json-файл

    Methods
    -------
    create():
        Создает json файлы со сгенерированными объектами.
    """

    def __init__(self,
                 vehicle_generator: VehicleGenerator,
                 number_of_objects: int = NUMBER_OF_OBJECTS,
                 number_of_objects_per_file: int = NUMBER_OF_OBJECTS_PER_FILE,
                 path: str = PATH,
                 include_none: bool = False):
        self.vehicle_generator = vehicle_generator
        self.number_of_objects = number_of_objects
        self.number_of_objects_per_file = number_of_objects_per_file
        self.path = path
        self.include_none = include_none

    def create(self):
        number_of_files = (self.number_of_objects + self.number_of_objects % self.number_of_objects_per_file) \
                          // self.number_of_objects_per_file
        for num in range(1, number_of_files + 1):
            filepath = f'{self.path}vehicle{num}.json'
            if number_of_files == 1:
                filepath = f'{self.path}vehicle.json'
            vehicles = [self.vehicle_generator.generate() for _ in range(self.number_of_objects_per_file)]
            with open(filepath, mode='w+') as file:
                json.dump(vehicles,
                          file,
                          default=lambda obj: obj.__getstate__(self.include_none),
                          indent=4,
                          ensure_ascii=False)


if __name__ == "__main__":
    json_creator = JsonCreator(
        VehicleGenerator(
            GuidGenerator(),
            StartDateGenerator(),
            EndDateGenerator(),
            StatusGenerator(),
            TypeGenerator(),
            BrandGenerator(),
            DriverGenerator(
                NameGenerator(),
                SurnameGenerator(),
                MiddleNameGenerator(),
                AgeGenerator(),
                PhoneNumberGenerator()
            )
        ),
        include_none=True
    )
    json_creator.create()
