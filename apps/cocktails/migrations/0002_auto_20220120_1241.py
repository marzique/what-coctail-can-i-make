# Generated by Django 3.0 on 2022-01-20 12:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='garnish',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, default=list, size=None),
        ),
    ]