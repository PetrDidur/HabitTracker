from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Поля модели привычек"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             **NULLABLE,
                             verbose_name='создатель привычки')
    place = models.CharField(max_length=150, verbose_name='место', **NULLABLE)
    time = models.TimeField(auto_now=False, verbose_name='время', **NULLABLE)
    action = models.TextField(verbose_name='действие', **NULLABLE)
    is_pleasant = models.BooleanField(verbose_name='приятная привычка', default=False)
    related_pleasant_habit = models.ForeignKey('self', on_delete=models.SET_NULL,
                                               verbose_name='связанная привычка', **NULLABLE)
    frequency = models.PositiveIntegerField(default=1, verbose_name='периодичность')
    reward = models.CharField(verbose_name='награда', max_length=150, **NULLABLE)
    completion_time = models.PositiveIntegerField(verbose_name='время на выполнение(минуты)', **NULLABLE)
    is_public = models.BooleanField(verbose_name='публичная привычка', default=False)

    def __str__(self):
        return f'{self.action} at {self.place} ({self.time}) by {self.user}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'





