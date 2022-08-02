from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.
class myUser(AbstractUser):
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password
