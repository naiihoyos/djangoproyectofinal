# Generated by Django 4.0.4 on 2022-05-15 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='cedula',
            field=models.IntegerField(default=0),
        ),
    ]
