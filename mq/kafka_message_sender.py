import json

from kafka import KafkaProducer

from generator.common import KafkaKeyGenerator

KAFKA_TOPIC = 'default_topic'
KAFKA_BROKERS = ('localhost:29092',)


class KafkaMessageSender:
    def __init__(self,
                 kafka_key_generator: KafkaKeyGenerator,
                 **kwargs):
        self.kafka_key_generator = kafka_key_generator
        self.kafka_topic = kwargs["kafka_topic"] if "kafka_topic" in kwargs else KAFKA_TOPIC
        self.kafka_brokers = kwargs["kafka_brokers"] if "kafka_brokers" in kwargs else KAFKA_BROKERS
        self.include_none = kwargs["include_none"] if "include_none" in kwargs else False

    def send(self, value):
        producer = KafkaProducer(bootstrap_servers=self.kafka_brokers,
                                 value_serializer=lambda x: bytes(
                                     json.dumps(x, default=lambda obj: obj.__getstate__(self.include_none)), "utf-8"),
                                 key_serializer=lambda x: bytes(x, 'utf-8'),
                                 max_request_size=100001200)
        producer.send(self.kafka_topic, key=self.kafka_key_generator.generate(), value=value).get()
        producer.flush()
        producer.close()
