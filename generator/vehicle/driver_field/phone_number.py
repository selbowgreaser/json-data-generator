import random
import string

COUNTRY_CODE = "+7"
LENGTH_NUMBER = 12


class PhoneNumberGenerator:
    """
    Класс для генерации случайного значения телефонного номера водителя.

    ...

    Attributes
    ----------
    country_code : str (default = COUNTRY_CODE)
        код страны телефонного номера
    length_number : int (default = LENGTH_NUMBER)
        длина телефонного номера

    Methods
    -------
    generate():
        Генерирует случайное значение телефонного номера водителя.
    """

    def __init__(self,
                 country_code: str = COUNTRY_CODE,
                 length_number: int = LENGTH_NUMBER):
        self.country_code = country_code
        self.length_number = length_number

    def generate(self):
        return f'{self.country_code + "".join(random.choices(string.digits, k=self.length_number - len(self.country_code)))}'


if __name__ == "__main__":
    phone_number_generator = PhoneNumberGenerator()
    print(phone_number_generator.generate())

    phone_number_generator_with_not_default_country_code = PhoneNumberGenerator("+0", 15)
    print(phone_number_generator_with_not_default_country_code.generate())
