from django.db import models
from django.contrib.auth.models import AbstractUser

from basemodels import BaseModel


class UserModel(AbstractUser):
    email = models.EmailField(unique=True)
