# Generated by Django 3.2 on 2021-05-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_alter_product_prdprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDPrice',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Product Price'),
        ),
    ]
