import datetime

from django.db import models

# Create your models here.
class Update(models.Model):
    text = models.CharField(max_length=120)
    date = models.DateField(default=datetime.date.today)