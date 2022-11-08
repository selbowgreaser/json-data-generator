from args_parser import ArgsParser
from mq import *
from generator.common.guid import *
from generator.vehicle import *
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
