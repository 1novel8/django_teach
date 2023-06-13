from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    email = models.EmailField(unique=True)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return str(self.username)
