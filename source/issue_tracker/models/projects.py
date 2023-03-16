from django.db import models
from django.utils import timezone


class Project(models.Model):
    created_at = models.DateField(verbose_name='Дата создания')
    completed_at = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='описание')
    is_deleted = models.BooleanField(default=False, verbose_name='удалено')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата и время удаления')

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
