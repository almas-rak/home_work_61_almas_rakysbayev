from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название')

    def __str__(self):
        return self.name
