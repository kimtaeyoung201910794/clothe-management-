from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('account.myUser',null=True,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    views = models.IntegerField()
    title = models.TextField(default = '')
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='images/',default = '')
