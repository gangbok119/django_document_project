# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0004_place_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champion_type', models.CharField(choices=[('magician', '마법사'), ('supporter', '서포터'), ('ad', '원거리 딜러')], max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('rank', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
