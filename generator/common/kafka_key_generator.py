import datetime
import json

import pytz

from generator.common import GuidGenerator


class KafkaKeyGenerator:
    def __init__(self,
                 guid_generator: GuidGenerator):
        self.guid_generator = guid_generator

    def generate(self) -> str:
        tz = pytz.timezone("Europe/Moscow")
        return json.dumps({"msgId": self.guid_generator.generate(),
                           "creationTime": f"{datetime.datetime.now(tz).strftime('%Y-%m-%dT%H:%M:%S')}+03:00"})


if __name__ == "__main__":
    print(KafkaKeyGenerator(GuidGenerator()).generate())
