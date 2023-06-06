# Generated by Django 4.2.2 on 2023-06-06 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0002_alter_document_filepath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='files_to_contrib',
        ),
        migrations.AddField(
            model_name='profile',
            name='files_to_review',
            field=models.ManyToManyField(blank=True, related_name='reviewers', to='web.document', verbose_name='Документы для рецензирования'),
        ),
        migrations.AlterField(
            model_name='discussiontext',
            name='author',
            field=models.CharField(max_length=200, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='discussiontext',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='discussiontext',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.document', verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='discussiontext',
            name='publish_date',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='document',
            name='filename',
            field=models.CharField(max_length=200, verbose_name='Имя файла'),
        ),
        migrations.AlterField(
            model_name='document',
            name='filepath',
            field=models.FilePathField(null=True, path=pathlib.PurePosixPath('/home/marselle/Саморазвитие/Project/EDMS_IITU/media'), verbose_name='Путь к файлу'),
        ),
        migrations.AlterField(
            model_name='document',
            name='signed',
            field=models.PositiveIntegerField(default=0, verbose_name='Подписано'),
        ),
        migrations.AlterField(
            model_name='document',
            name='signs_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество подписей'),
        ),
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(default='В процессе', max_length=25, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Одобрен'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='notifications',
            field=models.TextField(blank=True, verbose_name='Уведомления'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='personal_files',
            field=models.ManyToManyField(blank=True, related_name='owners', to='web.document', verbose_name='Личные документы'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
