# Generated by Django 3.2 on 2021-07-09 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0032_auto_20210706_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='paiment_type',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
