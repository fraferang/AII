# Generated by Django 3.1.3 on 2021-01-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210114_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='premios',
            field=models.TextField(verbose_name='Premios obtenidos'),
        ),
    ]
