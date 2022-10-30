from model import Driver


class Vehicle:
    """
    Класс для объекта Driver.

    ...

    Attributes
    ----------
    guid : str
       guid транспортного средства
    start_date : str
       дата начала эксплуатации транспортного средства
    brand : int (default = None)
       марка транспортного средства
    end_date : str (default = None)
        дата окончания эксплуатации транспортного средства
    status : str (default = None)
       статус эксплуатации транспортного средства
    vehicle_type (default = None)
        тип транспортного средства
    driver : Driver (default = None)
        объект водителя транспортного средства

    Methods
    -------
    set_end_date(end_date):
       Устанавливает дату начала эксплуатации транспортного средства для объекта Vehicle.
    set_status(status):
       Устанавливает статус эксплуатации транспортного средства для объекта Vehicle.
    set_vehicle_type(vehicle_type):
       Устанавливает тип транспортного средства для объекта Vehicle.
    set_driver(driver):
       Устанавливает объект водителя транспортного средства для объекта Vehicle.
    """

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

    def set_vehicle_type(self, vehicle_type: str):
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
