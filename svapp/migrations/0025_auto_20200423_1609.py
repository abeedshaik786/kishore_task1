# Generated by Django 2.2.10 on 2020-04-23 10:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svapp', '0024_auto_20200421_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the define format', regex='^\\+?1?\\d{9,12}$')]),
        ),
    ]