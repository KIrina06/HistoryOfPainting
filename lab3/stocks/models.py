from django.db import models

from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class User(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.surname

class Expertise(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.BinaryField()
    status = models.ForeignKey(to=Status, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Application(models.Model):
    status = models.ForeignKey(to=Status, on_delete=models.PROTECT)
    date_of_create = models.DateField()
    date_of_form = models.DateField()
    date_of_finish = models.DateField()
    moderator = models.ForeignKey(to=User, on_delete=models.PROTECT)

class ExpApp(models.Model):
    expertise = models.ForeignKey(to=Expertise, on_delete=models.PROTECT)
    application = models.ForeignKey(to=Application, on_delete=models.PROTECT)
