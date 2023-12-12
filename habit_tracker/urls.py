from django.urls import path

from habit_tracker.apps import HabitTrackerConfig
from rest_framework.routers import DefaultRouter

from habit_tracker.views import PublicHabitListAPIView, HabitCreateAPIView, HabitListAPIView, \
    HabitRetrieveAPIView, HabitUpdateAPIView, HabitDestroyAPIView

app_name = HabitTrackerConfig.name


urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/', HabitListAPIView.as_view(), name='habit-list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-get'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),

    path('public_habits/', PublicHabitListAPIView.as_view(), name='public_habits-list')
]

