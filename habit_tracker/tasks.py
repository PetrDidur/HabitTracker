
import os
from datetime import timedelta, datetime

from celery import shared_task
from django.utils import timezone

from habit_tracker.models import Habit
from habit_tracker.send_tg_message import send_telegram_notification


@shared_task
def send_habit_notification():
    now_time = timezone.now() + timedelta(hours=3)
    token = os.getenv('TG_BOT_TOKEN')
    habits_to_send = Habit.objects.filter(user__telegram_id__isnull=False).prefetch_related('user')

    for habit in habits_to_send:
        habit_time = datetime.combine(now_time.date(), habit.time)
        habit_time_aware = timezone.make_aware(habit_time, now_time.tzinfo)

        if habit_time_aware <= now_time - timedelta(minutes=5):
            message = (f'Через 5 минут необходимо выполнить действие {habit.action}'
                       f'После этого вы сможете вознаградить себя {habit.reward if habit.reward else habit.related_pleasant_habit}')
            send_telegram_notification(bot_token=token, chat_id=habit.user.telegram_id, message=message)



