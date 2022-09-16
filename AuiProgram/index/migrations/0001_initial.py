# Generated by Django 3.2 on 2022-02-17 08:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDDev', models.CharField(blank=True, max_length=20, null=True)),
                ('brand', models.CharField(blank=True, max_length=20, null=True)),
                ('SerialDev', models.CharField(blank=True, max_length=20, null=True)),
                ('typeDev', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDStud', models.CharField(blank=True, max_length=20, null=True)),
                ('NameStud', models.CharField(blank=True, max_length=20, null=True)),
                ('Duration', models.IntegerField()),
                ('DateRes', models.DateTimeField(default=datetime.datetime(2022, 2, 17, 9, 7, 40, 794100))),
                ('DateExp', models.DateTimeField(blank=True, null=True)),
                ('Device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.device', verbose_name='device')),
            ],
        ),
    ]
