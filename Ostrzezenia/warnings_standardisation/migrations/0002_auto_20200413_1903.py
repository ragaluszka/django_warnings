# Generated by Django 2.2.6 on 2020-04-13 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warnings_standardisation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warning',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
