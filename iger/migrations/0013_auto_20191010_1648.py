# Generated by Django 2.2.4 on 2019-10-10 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iger', '0012_remove_student_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listadepartamento',
            name='coordinacion',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listadepartamento',
            name='departamento',
            field=models.CharField(max_length=30),
        ),
    ]