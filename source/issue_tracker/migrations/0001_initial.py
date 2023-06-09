# Generated by Django 4.1.7 on 2023-03-19 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(verbose_name='Дата создания')),
                ('completed_at', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='описание')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='удалено')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время удаления')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
                ('user', models.ManyToManyField(blank=True, null=True, related_name='project_users', to=settings.AUTH_USER_MODEL, verbose_name='пользователи')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=100, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Полное описание')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата и время изменения')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время удаления')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='issue_tracker.project', verbose_name='Проект')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='status_task', to='issue_tracker.status', verbose_name='Статус')),
                ('type', models.ManyToManyField(related_name='type_task', to='issue_tracker.type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
