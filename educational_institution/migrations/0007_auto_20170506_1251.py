# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-06 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_institution', '0006_auto_20170506_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='educational_direction',
            name='educational_institution',
            field=models.ManyToManyField(to='educational_institution.Educational_institution'),
        ),
        migrations.AddField(
            model_name='educational_method',
            name='educational_institution',
            field=models.ManyToManyField(to='educational_institution.Educational_institution'),
        ),
        migrations.AddField(
            model_name='type_of_payment_for_education',
            name='educational_institution',
            field=models.ManyToManyField(to='educational_institution.Educational_institution'),
        ),
    ]
