# Generated by Django 5.1.4 on 2024-12-09 01:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0005_alter_board_messages_uuids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=120, unique=True),
        ),
    ]