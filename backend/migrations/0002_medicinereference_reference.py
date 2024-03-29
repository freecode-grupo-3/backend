# Generated by Django 3.2.11 on 2022-02-03 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified date')),
                ('place_of_origin_name', models.CharField(max_length=100, verbose_name='Place of origin name')),
                ('address_of_place_of_origin', models.CharField(max_length=255, verbose_name='Address of the place of origin')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('related_disease', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.disease')),
            ],
        ),
        migrations.CreateModel(
            name='MedicineReference',
            fields=[
                ('reference_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backend.reference')),
                ('name', models.CharField(max_length=100, verbose_name='Medicine name')),
                ('presentation', models.CharField(blank=True, max_length=100, verbose_name='Presentation of the medicine')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Price of the medicine')),
                ('currency', models.CharField(blank=True, choices=[('USD', 'Usd'), ('VES', 'Ves')], default=None, max_length=3, null=True)),
            ],
            bases=('backend.reference',),
        ),
    ]
