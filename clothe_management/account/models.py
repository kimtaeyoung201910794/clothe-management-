from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class myUser(AbstractUser):
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
