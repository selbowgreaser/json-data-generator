import random
import string

COUNTRY_CODE = "+7"
LENGTH_NUMBER = 12


class PhoneNumberGenerator:
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
