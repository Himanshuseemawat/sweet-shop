# Generated by Django 3.2 on 2022-05-26 21:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0002_alter_inquiry_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='phone_number',
            field=models.CharField(default=11111111111, max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')]),
            preserve_default=False,
        ),
    ]
