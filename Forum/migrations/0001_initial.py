# Generated by Django 5.1.4 on 2024-12-08 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=120)),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]