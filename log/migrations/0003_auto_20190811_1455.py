# Generated by Django 2.2.3 on 2019-08-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20190811_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='day',
            field=models.DateField(),
        ),
        migrations.DeleteModel(
            name='Day',
        ),
    ]
