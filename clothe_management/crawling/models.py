from django.db import models

# Create your models here.
class Crawling_image(models.Model):
    image = models.ImageField(upload_to='images/')