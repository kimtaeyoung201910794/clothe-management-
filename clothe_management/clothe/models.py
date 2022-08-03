from distutils.command.upload import upload
from turtle import color
from django.db import models

class clothe(models.Model):
    user = models.ForeignKey('account.myUser',null=True,on_delete=models.CASCADE)
    name = models.TextField(null=False, default = '')
    image = models.ImageField(upload_to='images/')
    season = models.TextField()
    category = models.TextField()
    favorite = models.BooleanField(default=False)
    color = models.TextField()
    style = models.TextField()
    memo = models.TextField()