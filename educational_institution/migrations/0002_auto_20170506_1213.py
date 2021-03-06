# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-06 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('educational_institution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.AlterField(
            model_name='educational_institution',
            name='license_for_educational_activity',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='educational_institution',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='educational_institution.City'),
        ),
    ]
