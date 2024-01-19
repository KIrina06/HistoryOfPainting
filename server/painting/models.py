from datetime import datetime

from django.contrib.auth.models import User, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone

from painting.utils.utils import format_time

class Expertises(models.Model):
    STATUS_CHOICES = (
        (1, 'Действует'),
        (2, 'Удалена'),
    )

    expertise_id = models.AutoField(primary_key=True)
    picture = models.CharField(blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=70, unique=True)
    price = models.CharField(blank=True, null=True)
    context = models.CharField(blank=True, null=True)
    expertise_status = models.IntegerField(choices=STATUS_CHOICES, default=1)

class Requests(models.Model):
    STATUS_CHOICES = (
        (1, 'Черновик'),
        (2, 'В работе'),
        (3, 'Завершен'),
        (4, 'Отклонен'),
        (5, 'Удален'),
    )

    request_id = models.BigAutoField(primary_key=True)
    expertises = models.ManyToManyField(Expertises)
    closed_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    formated_date = models.DateTimeField(blank=True, null=True)
    req_status = models.IntegerField(choices=STATUS_CHOICES, default=1)  # This field type is a guess.
    

class ReqExps(models.Model):
    expertise = models.ForeignKey('Expertises', models.DO_NOTHING, primary_key=True)
    request = models.ForeignKey('Requests', models.DO_NOTHING, primary_key=True)

    class Meta:
        unique_together = (('expertise', 'request'),)
