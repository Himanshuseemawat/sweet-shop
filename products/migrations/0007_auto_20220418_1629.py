# Generated by Django 3.2 on 2022-04-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20220413_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='year',
        ),
        migrations.AddField(
            model_name='product',
            name='popular_in_00s',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='popular_in_80s',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='popular_in_90s',
            field=models.BooleanField(default=False),
        ),
    ]