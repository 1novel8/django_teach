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
        through='AutoserviceRegularCustomersModel',
        related_query_name='autoservice_purchases_count',
        related_name='autoservice_purchases',
    )
    car_catalog = models.ManyToManyField(
        CarModel,
        through='AutoserviceCarCatalogModel',
        related_query_name='autoservice',  # whtf?
        related_name='autoservice',
    )
    sale_history = models.ManyToManyField(
        UserModel,
        through='AutoserviceSaleHistoryModel',
        related_query_name='buy_history',
        related_name='buy_history',
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


class AutoserviceCarCatalogModel(BaseModel):
    autoservice = models.ForeignKey(AutoserviceModel, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField(default=0)

    class Meta:
        db_table = 'autoservice_car_catalog'

    def __str__(self):
        return f'autoservice_id:{self.autoservice},' \
               f' car_id:{self.car},' \
               f' price:{self.price},' \
               f' count:{self.count}'


class AutoserviceRegularCustomersModel(BaseModel):
    autoservice = models.ForeignKey(AutoserviceModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    number_of_purchases = models.IntegerField(default=0)

    class Meta:
        db_table = 'autoservice_regular_customers'

    def __str__(self):
        return f'autoservice_id:{self.autoservice},' \
               f' user_id:{self.user},' \
               f' num_of_purchases:{self.number_of_purchases}'


class AutoserviceSaleHistoryModel(models.Model):
    autoservice = models.ForeignKey(AutoserviceModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    date_of_sale = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()

    class Meta:
        db_table = 'autoservice_sale_history'

    def __str__(self):
        return f'autoservice_id:{self.autoservice},' \
               f' user_id:{self.user},' \
               f' car_id:{self.car}'
