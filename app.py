import sys

from mq import *
from generator.common.guid import *
from generator.vehicle import *
from generator.vehicle.car_field import *
from generator.vehicle.driver_field import *

argv = sys.argv
mq_size = int(sys.argv[1]) if len(argv) > 1 else 999
time_interval = int(sys.argv[2]) if len(argv) > 2 else 0
print(f"Получено аргументов из командной строки: {len(argv) - 1}")
print(f"Будет отправлено {mq_size} сообщений с интервалом {time_interval} секунд")

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
        ),
        mq_size=mq_size,
        time_interval=time_interval
    ).run()
