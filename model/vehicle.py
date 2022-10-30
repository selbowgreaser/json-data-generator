from model import Driver


class Vehicle:
    def __init__(self,
                 guid: str,
                 start_date: str,
                 brand: str,
                 end_date: str = None,
                 status: str = None,
                 vehicle_type: str = None,
                 driver: Driver = None):
        self.guid = guid
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.vehicle_type = vehicle_type
        self.brand = brand
        self.driver = driver

    def set_end_date(self, end_date: str):
        self.end_date = end_date

    def set_status(self, status: str):
        self.status = status

    def set_type(self, vehicle_type: str):
        self.vehicle_type = vehicle_type

    def set_driver(self, driver: Driver):
        self.driver = driver

    def __str__(self):
        return str(self.__dict__)

    def __getstate__(self, include_none=True):
        return {key: value for key, value in self.__dict__.items() if include_none or value}


if __name__ == "__main__":
    vehicle = Vehicle("12345",
                      "1977-05-25",
                      "Ока")
    print(vehicle)
