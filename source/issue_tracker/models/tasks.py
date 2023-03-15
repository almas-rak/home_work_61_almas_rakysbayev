from django.db import models
from django.utils import timezone

from issue_tracker.models.statuses import Status
from issue_tracker.models.types import Type


class Task(models.Model):
    summary = models.CharField(max_length=100, verbose_name='Краткое описание')
    description = models.TextField(null=True, blank=True, verbose_name='Полное описание')
    status = models.ForeignKey(Status, related_name='status_task', on_delete=models.RESTRICT, verbose_name='Статус')
    type = models.ManyToManyField(Type, related_name='type_task', on_delete=models.RESTRICT, verbose_name='Тип')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата и время изменения')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата и время удаления')

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.summary
