from django.db import models


# Create your models here.
class Contact(models.Model):
    names = models.CharField(max_length=4000, default="")
    email = models.EmailField(default="")
    phone = models.CharField(max_length=10, default="")
    sem = models.CharField(max_length=455, default="")
    des = models.CharField(max_length=90000, default="")
    passwd = models.CharField(max_length=90000, default="")


