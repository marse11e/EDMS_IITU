# Generated by Django 4.2.1 on 2023-06-06 18:40

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='filepath',
            field=models.FilePathField(null=True, path=pathlib.PurePosixPath('/home/marselle/Саморазвитие/Project/EDMS_IITU/media')),
        ),
    ]
