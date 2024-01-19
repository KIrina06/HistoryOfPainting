from datetime import datetime

from django.contrib.auth.models import User, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone

from painting.utils.utils import format_time

class Paintings(models.Model):
    STATUS_CHOICES = (
        (1, 'Действует'),
        (2, 'Удалена'),
    )

    id = models.AutoField(primary_key=True)
    picture = models.CharField(blank=True, null=True)
    picture = models.BinaryField(blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=70, unique=True)
    price = models.CharField(blank=True, null=True)
    context = models.CharField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

class Expertises(models.Model):
    STATUS_CHOICES = (
        (1, 'Черновик'),
        (2, 'В работе'),
        (3, 'Завершена'),
        (4, 'Отклонена'),
        (5, 'Удалена'),
    )

    id = models.BigAutoField(primary_key=True)
    paintings = models.ManyToManyField(Paintings)
    closed_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    formated_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)  # This field type is a guess.
    artist = models.CharField(blank=True, null=True)
    

class PaintExps(models.Model):
    expertise = models.ForeignKey('Expertises', models.DO_NOTHING)
    painting = models.ForeignKey('Paintings', models.DO_NOTHING)

    class Meta:
        unique_together = (('expertise', 'painting'),)
