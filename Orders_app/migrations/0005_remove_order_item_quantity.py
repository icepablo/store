# Generated by Django 2.0.4 on 2018-07-21 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders_app', '0004_auto_20180721_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item_quantity',
        ),
    ]
