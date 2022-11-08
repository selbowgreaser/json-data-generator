import time

from generator.vehicle import VehicleGenerator
from mq import KafkaMessageSender

DEFAULT_MQ_SIZE = 999
DEFAULT_TIME_INTERVAL = 0


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

    def run(self):
        for i in range(1, self.mq_size + 1):
            value = self.vehicle_generator.generate()
            self.kafka_message_sender.send(value)
            print(f"\rОтправлено сообщений: {i}", end='')
            time.sleep(self.time_interval)
