from args_parser import ArgsParser
from mq import MqCreator, KafkaMessageSender
from generator.common import GuidGenerator, KafkaKeyGenerator
from generator.vehicle import VehicleGenerator, DriverGenerator
from generator.vehicle.car_field import *
from generator.vehicle.driver_field import *

kwargs = ArgsParser.get_args()

print(f"Получено {len(kwargs)} аргументов из командной строки: {kwargs}")

if __name__ == "__main__":
    MqCreator(
        KafkaMessageSender(
            KafkaKeyGenerator(
                GuidGenerator(),
            ),
            **kwargs
        ),
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
        **kwargs
    ).run()
