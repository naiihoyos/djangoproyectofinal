# Generated by Django 4.0.4 on 2022-05-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='ciudad',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='correo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='departamento',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='direccion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
