# Generated by Django 2.2.6 on 2020-04-13 19:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('warnings_standardisation', '0004_auto_20200413_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='warning',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='warning',
            name='date_now',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='warning',
            name='opis',
            field=models.TextField(default='PUSTY', max_length=1024),
        ),
        migrations.AlterField(
            model_name='warning',
            name='voltage',
            field=models.CharField(choices=[(1, '6kV'), (2, '15kv'), (3, '30kv'), (4, '110kV'), (5, 'Puste')], default=5, max_length=5),
        ),
    ]