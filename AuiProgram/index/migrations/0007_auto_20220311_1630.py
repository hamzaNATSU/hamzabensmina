# Generated by Django 3.2 on 2022-03-11 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20220310_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='Duration',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='DateRes',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 16, 30, 50, 203685)),
        ),
    ]
