from django.contrib.auth.models import AbstractUser
from django.db import models

from habit_tracker.models import NULLABLE


class User(AbstractUser):
    telegram_id = models.CharField(max_length=255, verbose_name=('Telegram ID'), **NULLABLE)