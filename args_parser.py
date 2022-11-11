import sys


class ArgsParser:
    
    @staticmethod
    def get_args() -> dict:
        argv = sys.argv
        kwargs = {}
        if "/s" in argv:
            mq_size_index = argv.index("/s") + 1
            kwargs.update({"mq_size": int(argv[mq_size_index])})
        if "/i" in argv:
            time_interval_index = argv.index("/i") + 1
            kwargs.update({"time_interval": int(argv[time_interval_index])})
        if "/t" in argv:
            topic_index = argv.index("/t") + 1
            kwargs.update({"kafka_topic": argv[topic_index]})
        if "/b" in argv:
            kafka_brokers_index = argv.index("/b") + 1
            kwargs.update({"kafka_brokers": argv[kafka_brokers_index]})
        if "/n" in argv:
            include_none_index = argv.index("/n") + 1
            kwargs.update({"include_none": True if argv[include_none_index] == 'Y' else False})
        if "/l" in argv:
            has_logging = argv.index("/l") + 1
            kwargs.update({"has_logging": True if argv[has_logging] == 'Y' else False})
        return kwargs
