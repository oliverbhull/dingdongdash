# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_buttonaction_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='buttonaction',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='button',
            name='description',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='button',
            name='name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
