import time

from generator.vehicle import VehicleGenerator
from mq import KafkaMessageSender


class MqCreator:
    def __init__(self,
                 kafka_message_sender: KafkaMessageSender,
                 vehicle_generator: VehicleGenerator,
                 mq_size: int,
                 time_interval: int,
                 ):
        self.kafka_message_sender = kafka_message_sender
        self.vehicle_generator = vehicle_generator
        self.mq_size = mq_size
        self.time_interval = time_interval

    def run(self):
        for i in range(1, self.mq_size + 1):
            value = self.vehicle_generator.generate()
            self.kafka_message_sender.send(value)
            print(f"\rОтправлено сообщений: {i}", end='')
            time.sleep(self.time_interval)
