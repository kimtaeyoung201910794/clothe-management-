from distutils.command.upload import upload
from turtle import color
from django.db import models

class clothe(models.Model):
    user = models.ForeignKey('account.myUser',on_delete=models.CASCADE)
    name = models.TextField(null=False, default = '')
    image = models.ImageField(upload_to='images/')
    season = models.TextField()
    parent_category = models.TextField(default='')
    child_category = models.TextField(default='')
    favorite = models.BooleanField(default=False)
    color = models.TextField()
    style = models.TextField()
    memo = models.TextField()

class looks(models.Model):
    user = models.ForeignKey('account.myuser',on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=100,null=False)
    top = models.ForeignKey(clothe,on_delete=models.CASCADE,null=False,related_name='top')
    bottom = models.ForeignKey(clothe,on_delete=models.CASCADE,null=False,related_name='bottom')
    shoes = models.ForeignKey(clothe,on_delete=models.CASCADE,null=False,related_name='shoes')
    ACC1 = models.ForeignKey(clothe,on_delete=models.CASCADE,null=True,related_name='ACC1')
    ACC2 = models.ForeignKey(clothe,on_delete=models.CASCADE,null=True,related_name='ACC2')