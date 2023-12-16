import requests
from django.conf import settings


def send_telegram_notification(bot_token, chat_id, message):
    api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}

    response = requests.post(api_url, params=params)
    return response.json()