from django.db import models
from django_countries.fields import CountryField

from basemodels import BaseModel
from Authentication.models import UserModel


class CarModel(BaseModel):
    class Brand(models.TextChoices):
        BMW = 'BMW', 'BMW'
        AUDI = 'AUDI', 'Audi'
        BUGATTI = 'BUGATTI', 'Bugatti'
        CADILLAC = 'CADILLAC', 'Cadillac'
        CHEVROLET = 'CHEVROLET', 'Chevrolet'
        CITROEN = 'CITROEN', 'Citroen'
        FERRARI = 'FERRARI', 'Ferrari'
        FORD = 'FORD', 'Ford'
        LEXUS = 'LEXUS', 'Lexus'

    class FuelType(models.TextChoices):
        PETROL = 'PETROL', 'petrol'
        DISEL = 'DISEL', 'disel'
        CNG = 'CNG', 'CNG'
        BIO_DISEL = 'BIO_DISEL', 'bio disel'
        ELECTRIC = 'ELECTRIC', 'electric'

    name = models.CharField(max_length=20)
    brand = models.CharField(choices=Brand.choices, max_length=20)
    fuel_type = models.CharField(choices=FuelType.choices, max_length=20)

    class Meta:
        db_table = 'car'

    def __str__(self):
        return f'id:{self.id},' \
               f' name:{self.name},' \
               f' brand:{self.brand},' \
               f' fuel:{self.fuel_type}'


class AutoserviceModel(BaseModel):
    name = models.CharField(max_length=20, verbose_name='name')
    balance = models.IntegerField(default=0, verbose_name='balance')
    country = CountryField()
    regular_customers = models.ManyToManyField(
        UserModel,
        through='AutoserviceRegularCustomers',
        related_query_name='autoservices'
    )

    class Meta:
        db_table = 'autoservice'

    def __str__(self):
        return f'id:{self.id},' \
               f' name:{self.name},' \
               f' balance:{self.balance},' \
               f' country:{self.country}'


class PreferredCarParametersModel(BaseModel):
    autoservice = models.OneToOneField(
        AutoserviceModel,
        on_delete=models.CASCADE,
        related_name='preferred_car_parameters'
    )
    brand = models.CharField(choices=CarModel.Brand.choices, max_length=20)
    fuel_type = models.CharField(choices=CarModel.FuelType.choices, max_length=20)

    class Meta:
        db_table = 'preferred_car_parameters'

    def __str__(self):
        return f'autoservice_id:{self.autoservice},' \
               f' brand:{self.brand},' \
               f' fuel:{self.fuel_type}'


class AutoserviceRegularCustomers(BaseModel):
    autoservice = models.ForeignKey(AutoserviceModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    number_of_purchases = models.IntegerField(default=0)

    class Meta:
        db_table = 'autoservice_regular_customers'

    def __str__(self):
        return f'autoservice_id:{self.autoservice},' \
               f' user_id:{self.user},' \
               f' num_of_purchases:{self.number_of_purchases}'
