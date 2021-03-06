# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170330_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apilog',
            options={'verbose_name': 'API Log', 'verbose_name_plural': 'API Logs'},
        ),
        migrations.AlterModelOptions(
            name='buttonaction',
            options={'verbose_name': 'Action', 'verbose_name_plural': 'Actions'},
        ),
        migrations.RenameField(
            model_name='buttonaction',
            old_name='phone',
            new_name='target_user',
        ),
        migrations.AlterField(
            model_name='buttonaction',
            name='type',
            field=models.CharField(choices=[('message', 'Send SMS Message'), ('call', 'Make Voice Call'), ('email', 'Send Email')], default='call', max_length=8),
        ),
    ]
