# Generated by Django 3.2.7 on 2021-09-08 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buoys', '0004_auto_20210908_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buoy',
            name='downtime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='buoy',
            name='startup',
            field=models.DateTimeField(),
        ),
    ]
