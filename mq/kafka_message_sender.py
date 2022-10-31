from kafka import KafkaProducer

from mq import KafkaKeyGenerator

KAFKA_TOPIC = 'default_topic'
KAFKA_BROKERS = ('localhost:29092',)


class KafkaMessageSender:
    def __init__(self,
                 kafka_key_generator: KafkaKeyGenerator,
                 kafka_topic: str = KAFKA_TOPIC,
                 kafka_brokers: list = KAFKA_BROKERS,
                 include_none: bool = False):
        self.kafka_key_generator = kafka_key_generator
        self.kafka_topic = kafka_topic
        self.kafka_brokers = kafka_brokers
        self.include_none = include_none

    def send(self, value):
        producer = KafkaProducer(bootstrap_servers=self.kafka_brokers,
                                 value_serializer=lambda x: bytes(str(x.__getstate__(self.include_none)), 'utf-8'),
                                 key_serializer=lambda x: bytes(x, 'utf-8'),
                                 max_request_size=100001200)
        producer.send(self.kafka_topic, key=self.kafka_key_generator.generate(), value=value).get()
        producer.flush()
        producer.close()
