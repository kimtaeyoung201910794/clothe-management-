from django.db import models

class ChatRoom(models.Model):
    users = models.ForeignKey('account.myUser',on_delete=models.CASCADE)

class Message(models.Model):
    users = models.OneToOneField('account.myUser',on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
