# Generated by Django 3.1.3 on 2021-01-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='ranking',
            field=models.TextField(verbose_name='Ranking actual'),
        ),
    ]
