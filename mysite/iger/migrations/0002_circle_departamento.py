# Generated by Django 2.2.3 on 2019-08-13 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('circle_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name_coor', models.CharField(max_length=20)),
                ('id_coor', models.IntegerField()),
                ('num_x', models.IntegerField()),
                ('circle_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('coordinacion', models.IntegerField()),
                ('departamento', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]
