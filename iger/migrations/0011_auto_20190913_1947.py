# Generated by Django 2.2.4 on 2019-09-14 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iger', '0010_auto_20190913_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='coordinacion',
            field=models.CharField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]