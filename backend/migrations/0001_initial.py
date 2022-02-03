# Generated by Django 3.2.11 on 2022-02-03 05:29

from django.db import migrations, models

def populate_diseases(apps, schema_editor):
    """
        Populate the disease database with some samples
    """
    Disease = apps.get_model('backend', 'Disease')

    diseases = [
        ('neutropenia', 'es una disminución en la cantidad de glóbulos blancos'),
        ('septicemia','es una complicación causada por la respuesta abrumadora y potencialmente mortal del cuerpo a una infección')
    ]

    Disease.objects.bulk_create(
        Disease(name=name, description=descp)
        for name, descp in diseases
    )



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Name of the disease')),
                ('description', models.CharField(max_length=512, verbose_name='Description of the disease')),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Reference type name')),
                ('description', models.CharField(max_length=512, verbose_name='Description of the reference type')),
            ],
        ),
        migrations.RunPython(populate_diseases, migrations.RunPython.noop),
    ]
