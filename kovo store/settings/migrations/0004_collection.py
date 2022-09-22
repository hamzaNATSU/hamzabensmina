# Generated by Django 3.2 on 2021-05-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_intads_intadate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CLTName', models.CharField(max_length=15, verbose_name='Collection Title (part1) ')),
                ('CLTName2', models.CharField(max_length=15, verbose_name='Collection Title(part 2) ')),
                ('CLTDesc', models.TextField(blank=True, null=True, verbose_name='description:')),
                ('INTAImg', models.ImageField(blank=True, null=True, upload_to='Clts_images/')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
    ]
