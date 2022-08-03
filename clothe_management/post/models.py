from django.db import models
from datetime import datetime, timedelta

class Post(models.Model):
    board = models.CharField(max_length=100,default='')
    likes = models.IntegerField(default = 0)
    annonymous = models.BooleanField(default = False)
    user = models.ForeignKey('account.myUser',null=True,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    views = models.IntegerField()
    title = models.TextField(default = '')
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='images/',default = '')

    @property
    def created_string(self):

        time = datetime.now() - self.time

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now().date() - self.time.date()
            return str(time.days) + '일 전'
        else:
            return False
    @property
    def writer(self):
        if self.annonymous:
            return self.user.first_name+self.user.last_name
        else:
            return '익명'
