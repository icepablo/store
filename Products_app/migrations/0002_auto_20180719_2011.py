# Generated by Django 2.0.4 on 2018-07-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=None),
        ),
    ]
