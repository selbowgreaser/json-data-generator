import random

DEFAULT_BRANDS = (
    'Dacia', 'Hyundai', 'Maybach', 'Peugeot', 'Hummer', 'УАЗ', 'Alfa Romeo', 'Chrysler', 'Lexus', 'Toyota',
    'Aston Martin', 'Bentley', 'Daihatsu', 'Rolls-Royce', 'Volvo', 'Lifan', 'Ford', 'Lotus', 'Chery', 'ВАЗ',
    'Mercedes', 'Ferrari', 'Mini', 'Dodge', 'Москвич', 'Maserati', 'Genesis', 'Faw', 'GMC', 'Smart', 'Cadillac',
    'Audi', 'Ssangyong', 'Lancia', 'Brilliance', 'Volkswagen', 'Daewoo', 'Changan', 'Renault', 'Kia', 'ЗАЗ',
    'Porsche', 'Haval', 'Exeed', 'Citroen', 'Rover', 'Pontiac', 'Chevrolet', 'Mclaren', 'Mitsubishi', 'Opel',
    'Tagaz', 'Seat', 'Bugatti', 'Honda', 'Jaguar', 'Land Rover', 'Geely', 'Datsun', 'ГАЗ', 'Great Wall',
    'Marussia', 'Suzuki', 'Lamborghini', 'Jeep', 'Subaru', 'BMW', 'Tesla', 'Мотоцикл', 'Buick', 'Nissan', 'Mazda',
    'Infiniti', 'Lincoln', 'Skoda', 'Saab', 'Fiat', 'Acura')


class BrandGenerator:
    """
    Класс для случайного выбора марки транспортного средства.

    ...

    Attributes
    ----------
    available_brands : tuple (default = DEFAULT_BRANDS)
        коллекция возможных марок транспортных средств

    Methods
    -------
    generate():
        Генерирует случайное значение марки транспортного средства.
    """

    def __init__(self,
                 available_brands: tuple = DEFAULT_BRANDS):
        self.available_brands = available_brands

    def generate(self) -> str:
        return random.choice(self.available_brands)


if __name__ == "__main__":
    brand_generator = BrandGenerator()
    print(brand_generator.generate())

    brand_generator_with_my_brands = BrandGenerator(('Porsche', 'Lamborghini', 'Ferrari'))
    print(brand_generator_with_my_brands.generate())
