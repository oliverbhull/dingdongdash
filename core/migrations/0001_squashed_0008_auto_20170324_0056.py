# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 03:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [(b'core', '0001_initial'), (b'core', '0002_auto_20170323_1559'), (b'core', '0003_button_organizations'), (b'core', '0004_auto_20170323_1901'), (b'core', '0005_auto_20170323_1905'), (b'core', '0006_auto_20170323_2310'), (b'core', '0007_phone'), (b'core', '0008_auto_20170324_0056')]

    initial = True

    dependencies = [
        ('organizations', '0002_model_update'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=16, unique=True)),
                ('double_press_action', models.CharField(choices=[('message', 'Send SMS Message'), ('call', 'Make Voice Call')], default='message', max_length=8)),
                ('long_press_action', models.CharField(choices=[('message', 'Send SMS Message'), ('call', 'Make Voice Call')], default='call', max_length=8)),
                ('single_press_action', models.CharField(choices=[('message', 'Send SMS Message'), ('call', 'Make Voice Call')], default='call', max_length=8)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
