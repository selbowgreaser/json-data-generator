from mq import *
from generator.common.guid import *
from generator.vehicle import *
from generator.vehicle.car_field import *
from generator.vehicle.driver_field import *

if __name__ == "__main__":
    MqCreator(
        KafkaMessageSender(
            KafkaKeyGenerator(
                GuidGenerator()
            )
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
        )
    ).run()
