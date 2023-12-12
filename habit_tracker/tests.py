from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit_tracker.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            username='admin',
            is_active=True
        )

        self.user.set_password('9184')
        self.user.save()

        get_token = reverse('users:token_obtain_pair')
        token_response = self.client.post(path=get_token, data={'username': 'admin', 'password': '9184'})
        token = token_response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

        self.habit = Habit.objects.create(
            id=3,
            action='drink water',
            is_pleasant=True,
            frequency=7,
            is_public=True
        )

    def test_get_list(self):

        response = self.client.get(
            reverse('habit:habit-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 0,
                "next": None,
                "previous": None,
                "results": [

                ]
            }
        )

    def test_lesson_create(self):
        """Test lesson creating"""

        data = {
            "action": "drink water",
            "is_pleasant": True,
            "frequency": 7,
            "is_public": True
        }

        response = self.client.post(
            reverse('habit:habit_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Habit.objects.all().count(),
            2
        )

    def test_habit_retrieve(self):
            url = reverse('habit:habit-get', args=[self.habit.id])
            response = self.client.get(url)
            print(response.json())

            self.assertEqual(response.status_code, status.HTTP_200_OK)


class PublicHabitTestCase(APITestCase):
    def setUp(self) -> None:

        self.user = User.objects.create(
            username='admin',
            is_active=True
        )

        self.user.set_password('9184')
        self.user.save()

        get_token = reverse('users:token_obtain_pair')
        token_response = self.client.post(path=get_token, data={'username': 'admin', 'password': '9184'})
        token = token_response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

        self.habit = Habit.objects.create(
            action='drink water',
            is_pleasant=True,
            frequency=7,
            is_public=True
        )

    def test_get_list(self):

        response = self.client.get(
            reverse('habit:public_habits-list')
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
                    {
                        "id": self.habit.id,
                        "place": None,
                        "is_pleasant": False,
                        "reward": self.habit.reward,
                        "is_public": True,
                        "user": self.habit.user_id,
                        "related_pleasant_habit": None
                    }
        )






