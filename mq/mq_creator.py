import time

from generator.vehicle import VehicleGenerator
from mq import KafkaMessageSender


class MqCreator:
    def __init__(self,
                 kafka_message_sender: KafkaMessageSender,
                 vehicle_generator: VehicleGenerator,
                 mq_size: int = 999,
                 time_interval: int = 0,
                 ):
        self.kafka_message_sender = kafka_message_sender
        self.vehicle_generator = vehicle_generator
        self.mq_size = mq_size
        self.time_interval = time_interval

    def run(self):
        for _ in range(self.mq_size):
            value = self.vehicle_generator.generate()
            self.kafka_message_sender.send(value)
            time.sleep(self.time_interval)
