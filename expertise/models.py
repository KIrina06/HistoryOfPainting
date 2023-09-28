from django import utils
from django.db import models
from datetime import date

class Status(models.Model):
    name = models.CharField(max_length=120, unique=True)
    
    def __str__(self):
        return self.name

class User(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20)

class Expertise(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='static')
    status = models.ForeignKey(to=Status, on_delete=models.PROTECT)
    

class Application(models.Model):
    status = models.ForeignKey(to=Status, on_delete=models.PROTECT)
    date_of_create = models.DateField(default=utils.timezone.now)
    date_of_form = models.DateField(default=utils.timezone.now)
    date_of_finish = models.DateField(default=utils.timezone.now)
    moderator = models.ForeignKey(to=User, on_delete=models.PROTECT)

class ExpApp(models.Model):
    expertise = models.ForeignKey(to=Expertise, on_delete=models.PROTECT)
    application = models.ForeignKey(to=Application, on_delete=models.PROTECT)

