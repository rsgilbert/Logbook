# Generated by Django 2.2.3 on 2019-08-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20190811_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='day',
            field=models.CharField(max_length=100),
        ),
    ]
