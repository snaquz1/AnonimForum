import datetime

import uuid
from django.db import models

# Create your models here.
class Update(models.Model):
    text = models.CharField(max_length=120)
    date = models.DateField(default=datetime.date.today)

class Board(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, blank=False, unique=True, editable=False)
    name = models.CharField(max_length=120)
    creation_date = models.DateField(default=datetime.date.today)
    messages_uuids = models.TextField()

class Message(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, blank=False, unique=True, editable=False)
    datetime = models.DateTimeField(default=datetime.datetime.now)
    text = models.TextField()

