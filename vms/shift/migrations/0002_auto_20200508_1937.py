# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-08 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0001_initial'),
        ('cities_light', '0008_city_timezone'),
        ('shift', '0001_initial'),
        ('volunteer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteershift',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer.Volunteer'),
        ),
        migrations.AddField(
            model_name='shift',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City'),
        ),
        migrations.AddField(
            model_name='shift',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country'),
        ),
        migrations.AddField(
            model_name='shift',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Job'),
        ),
        migrations.AddField(
            model_name='shift',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Region'),
        ),
        migrations.AddField(
            model_name='shift',
            name='volunteers',
            field=models.ManyToManyField(through='shift.VolunteerShift', to='volunteer.Volunteer'),
        ),
        migrations.AddField(
            model_name='report',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer.Volunteer'),
        ),
        migrations.AddField(
            model_name='report',
            name='volunteer_shifts',
            field=models.ManyToManyField(to='shift.VolunteerShift'),
        ),
        migrations.AddField(
            model_name='editrequest',
            name='volunteer_shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shift.VolunteerShift'),
        ),
    ]
