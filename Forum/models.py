import datetime

import uuid
from django.db import models

# Create your models here.
class Update(models.Model):
    text = models.CharField(max_length=120)
    date = models.DateField(default=datetime.date.today)

class Board(models.Model):
    uuid = models.CharField(default=uuid.uuid4, blank=False, unique=True, editable=False, max_length=120)
    name = models.CharField(max_length=120)
    creation_date = models.DateField(default=datetime.date.today)
    messages_uuids = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to="images/")

class Message(models.Model):
    uuid = models.CharField(default=uuid.uuid4, blank=False, unique=True, editable=False, max_length=120)
    datetime = models.DateTimeField(default=datetime.datetime.now)
    text = models.TextField()

