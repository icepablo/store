# Generated by Django 2.0.4 on 2018-07-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products_app', '0004_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
