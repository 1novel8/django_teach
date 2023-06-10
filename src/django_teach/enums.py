from enum import Enum


class Brand(Enum):
    BMW = 'BMW'
    AUDI = 'Audi'
    BUGATTI = 'Bugatti'
    CADILLAC = 'Cadillac'
    CHEVROLET = 'Chevrolet'
    CITROEN = 'Citroen'
    FERRARI = 'Ferrari'
    FORD = 'Ford'
    LEXUS = 'Lexus'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class FuelType(Enum):
    petrol = 'petrol'
    disel = 'disel'
    CNG = 'CNG'
    bio_disel = 'bio disel'
    electric = 'electric'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
