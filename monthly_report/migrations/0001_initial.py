# Generated by Django 4.0.2 on 2022-02-27 11:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(blank=True, max_length=100)),
                ('street', models.CharField(blank=True, max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MemberData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('cnic', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9+]{5}-[0-9+]{7}-[0-9]{1}$', 'Not a valid C.N.I.C.')])),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('status_in_jamaat', models.CharField(choices=[('karkun', 'karkun'), ('umeedwar', 'umeedwar'), ('rukn', 'rukn')], max_length=15)),
                ('designation', models.CharField(max_length=100)),
                ('facebook_url', models.URLField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monthly_report.address')),
            ],
        ),
    ]
