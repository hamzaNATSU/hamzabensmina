# Generated by Django 3.2 on 2022-02-17 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='Reserved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='DateRes',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 17, 11, 57, 28, 850562)),
        ),
    ]
