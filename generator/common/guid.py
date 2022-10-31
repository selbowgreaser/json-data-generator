import random
import string

TEMPLATE_GUID = (8, 4, 4, 4, 12)


class GuidGenerator:
    """
    Класс для генерации случайного значения guid.

    ...

    Attributes
    ----------
    template_guid : tuple (default = TEMPLATE_GUID)
        шаблон представления guid
    lowercase_letters_flag : bool (default = True)
        флаг включения в список доступных символов букв в нижнем регистре
    uppercase_letters_flag : bool (default = True)
        флаг включения в список доступных символов букв в верхнем регистре
    digits_flag : bool (default = True)
        флаг включения в список доступных символов цифр

    Methods
    -------
    generate():
        Генерирует случайное значение guid по шаблону.
    """

    def __init__(self,
                 template_guid: tuple = TEMPLATE_GUID,
                 lowercase_letters_flag: bool = True,
                 uppercase_letters_flag: bool = True,
                 digits_flag: bool = True):
        self.template_guid = template_guid
        self.available_characters = string.ascii_lowercase * lowercase_letters_flag \
                                    + string.ascii_uppercase * uppercase_letters_flag \
                                    + string.digits * digits_flag

    def generate(self):
        return "-".join(["".join(random.choices(self.available_characters, k=i))
                         for i in self.template_guid])


if __name__ == "__main__":
    guid_generator = GuidGenerator()
    print(guid_generator.generate())

    guid_generator_with_not_default_template = GuidGenerator((5, 5, 5, 5))
    print(guid_generator_with_not_default_template.generate())

    guid_generator_without_uppercase_letters = GuidGenerator((5, 5, 5, 5), uppercase_letters_flag=False)
    print(guid_generator_without_uppercase_letters.generate())

    guid_generator_without_lowercase_letters = GuidGenerator((5, 5, 5, 5), lowercase_letters_flag=False)
    print(guid_generator_without_lowercase_letters.generate())

    guid_generator_without_digits = GuidGenerator((5, 5, 5, 5), digits_flag=False)
    print(guid_generator_without_digits.generate())
