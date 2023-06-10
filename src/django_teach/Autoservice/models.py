from django.db import models
from django_countries.fields import CountryField

from basemodels import BaseModel
from enums import Brand, FuelType


class CarModel(BaseModel):
    name = models.CharField(max_length=20)
    brand = models.CharField(choices=Brand.choices())
    fuel_type = models.CharField(choices=FuelType.choices())

    class Meta:
        db_table = 'car'

    def __str__(self):
        return f'id:{self.id}, name:{self.name}, brand:{self.brand}, fuel:{self.fuel_type}'


class AutoserviceModel(BaseModel):
    name = models.CharField(max_length=20, verbose_name='name')
    balance = models.IntegerField(default=0, verbose_name='balance')
    country = CountryField()

    class Meta:
        db_table = 'autoservice'

    def __str__(self):
        return f'id:{self.id}, name:{self.name}, balance:{self.balance}, country:{self.country}'


class PreferredCarParametersModel(models.Model):
    autoservice = models.OneToOneField(
        AutoserviceModel,
        on_delete=models.CASCADE,
        related_name='preferred_car_parameters'
    )
    brand = models.CharField(choices=Brand.choices())
    fuel_type = models.CharField(choices=FuelType.choices())

    class Meta:
        db_table = 'preferred_car_parameters'

    def __str__(self):
        return f'autoservice_id:{self.autoservice}, brand:{self.brand}, fuel:{self.fuel_type}'
