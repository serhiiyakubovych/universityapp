# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-06 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_institution', '0007_auto_20170506_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.ManyToManyField(to='educational_institution.Faculty'),
        ),
    ]
