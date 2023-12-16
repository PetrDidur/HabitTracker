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
            user=self.user,
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
        self.assertEqual(
            response.json(),
            {
                "user": 1,
                "action": 'drink water',
                "is_pleasant": True,
                "completion_time": None,
                "frequency": 7,
                "id": 1,
                "is_public": True,
                "place": None,
                "related_pleasant_habit": None,
                "reward": None,
                "time": None
                }
            )

    def test_habit_update(self):
        update_url = reverse('habit:habit-update', args=[self.habit.id])

        new_data = {
                    "user": 1,
                    "action": 'drink vodka',
                    "time": "10:00",
                    "place": "garage",
                    "frequency": 7,
                    }
        response = self.client.put(update_url, data=new_data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_habit = Habit.objects.get(id=self.habit.id)
        self.assertEqual(updated_habit.action, new_data['action'])

    def test_habit_delete(self):
        delete_url = reverse('habit:habit-delete', args=[self.habit.id])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())


class HabitPublicListAPIView(APITestCase):
    def setUp(self):
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

        self.habit1 = Habit.objects.create(
            user=self.user,
            action='drink water',
            is_pleasant=True,
            frequency=7,
            is_public=True
        )

        self.habit2 = Habit.objects.create(
            user=self.user,
            action='drink juice',
            is_pleasant=True,
            frequency=7,
            is_public=True
        )

    def test_get_habit_list(self):
        list_url = reverse('habit:habit-list')

        response = self.client.get(list_url)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)










