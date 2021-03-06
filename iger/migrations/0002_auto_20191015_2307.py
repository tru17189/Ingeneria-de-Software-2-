# Generated by Django 2.2.4 on 2019-10-16 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaDepartamento',
            fields=[
                ('coordinacion', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('departamento', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_carnet',
            new_name='carnet',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_grade',
            new_name='grado',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_semester',
            new_name='semestre',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_name',
        ),
        migrations.AddField(
            model_name='student',
            name='nombre_completo',
            field=models.CharField(default=0, max_length=35),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('codigo_circulo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('coordinacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iger.ListaDepartamento')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='circulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='iger.Circle'),
        ),
    ]
