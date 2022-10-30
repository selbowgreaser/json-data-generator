import json

from vehicle_field_generator import VehicleGenerator, DriverGenerator
from vehicle_field_generator.car_field_generator import *
from vehicle_field_generator.driver_field_generator import *

NUMBER_OF_OBJECTS = 100
NUMBER_OF_OBJECTS_PER_FILE = 100
PATH = r"json\\vehicle"


class JsonCreator:
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
            if number_of_files != 1:
                with open(fr'{self.path}{num}.json', mode='w+') as file:
                    vehicles = [self.vehicle_generator.generate() for _ in range(self.number_of_objects_per_file)]
                    json.dump(vehicles,
                              file,
                              default=lambda obj: obj.__getstate__(self.include_none),
                              indent=4,
                              ensure_ascii=False)
            else:
                with open(fr'{self.path}.json', mode='w+') as file:
                    vehicles = [self.vehicle_generator.generate() for _ in range(self.number_of_objects_per_file)]
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
