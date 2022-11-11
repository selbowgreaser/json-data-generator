import time

from generator.vehicle import VehicleGenerator
from mq import KafkaMessageSender

DEFAULT_MQ_SIZE = None
DEFAULT_TIME_INTERVAL = 5


class MqCreator:
    def __init__(self,
                 kafka_message_sender: KafkaMessageSender,
                 vehicle_generator: VehicleGenerator,
                 **kwargs
                 ):
        self.kafka_message_sender = kafka_message_sender
        self.vehicle_generator = vehicle_generator
        self.mq_size = kwargs["mq_size"] if "mq_size" in kwargs else DEFAULT_MQ_SIZE
        self.time_interval = kwargs["time_interval"] if "time_interval" in kwargs else DEFAULT_TIME_INTERVAL
        self.has_logging = kwargs["has_logging"] if "has_logging" in kwargs else False

    def run(self):
        if self.mq_size:
            print(f'Будет отправлено {self.mq_size} сообщений')
            for i in range(1, self.mq_size + 1):
                value = self.vehicle_generator.generate()
                self.kafka_message_sender.send(value)
                if self.has_logging is True:
                    print(f"\rОтправлено сообщений: {i}", end='')
                time.sleep(self.time_interval)
        else:
            print(f'Генератор запущен без ограничения сообщений')
            count_sent_messages = 0
            while True:
                value = self.vehicle_generator.generate()
                self.kafka_message_sender.send(value)
                count_sent_messages += 1
                if self.has_logging is True:
                    print(f"\rОтправлено сообщений: {count_sent_messages}", end='')
                time.sleep(self.time_interval)
