# Generated by Django 3.2 on 2022-03-10 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_reservation_dateres'),
    ]

    operations = [
        migrations.CreateModel(
            name='email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='reservation',
            name='DateRes',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 10, 16, 15, 48, 123073)),
        ),
    ]
