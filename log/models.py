from django.db import models
from django import forms

# Create your models here.

class Log(models.Model):
    day = models.CharField(max_length=100)
    activities = models.CharField(max_length=300)
    plans = models.CharField(max_length=300)

    def __str__(self):
        return self.activities

