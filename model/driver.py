class Driver:
    def __init__(self,
                 name: str,
                 surname: str,
                 age: int = None,
                 middle_name: str = None,
                 phone_number: str = None):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.age = age
        self.phone_number = phone_number

    def set_middle_name(self, middle_name: str):
        self.middle_name = middle_name

    def set_phone_number(self, phone_number: str):
        self.phone_number = phone_number

    def __getstate__(self, include_none=True):
        return {key: value for key, value in self.__dict__.items() if include_none or value}


if __name__ == "__main__":
    driver = Driver("Александр",
                    "Фролов",
                    22)
    print(driver)
