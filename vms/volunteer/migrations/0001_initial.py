# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-08 19:37
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
        ('cities_light', '0008_city_timezone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[(A-Z)|(a-z)|(\\s)|(\\-)]+$')])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[(A-Z)|(a-z)|(\\s)|(\\-)]+$')])),
                ('address', models.CharField(max_length=75, validators=[django.core.validators.RegexValidator('^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\-)|(\\.)|(,)|(\\:)]+$')])),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\s*(?:\\+?(\\d{1,3}))?([-. (]*(\\d{3})[-. )]*)?((\\d{3})[-. ]*(\\d{2,4})(?:[-.x ]*(\\d+))?)\\s*$', message='Please enter a valid phone number')])),
                ('email', models.EmailField(max_length=45, unique=True)),
                ('websites', models.TextField(blank=True, validators=[django.core.validators.RegexValidator('^(https?:\\/\\/(?:www\\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\\.[^\\s]{2,}|www\\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\\.[^\\s]{2,}|https?:\\/\\/(?:www\\.|(?!www))[a-zA-Z0-9]\\.[^\\s]{2,}|www\\.[a-zA-Z0-9]\\.[^\\s]{2,})+$')])),
                ('description', models.TextField(blank=True, validators=[django.core.validators.RegexValidator('^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\.)|(,)|(\\-)|(!)]+$')])),
                ('resume', models.TextField(blank=True, validators=[django.core.validators.RegexValidator('^[(A-Z)|(a-z)|(0-9)|(\\s)|(\\.)|(,)|(\\-)|(!)]+$')])),
                ('resume_file', models.FileField(blank=True, max_length=75, upload_to='vms/resume/')),
                ('reminder_days', models.IntegerField(blank=True, default=1, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)])),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Country')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Organization')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.Region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
