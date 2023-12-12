
from rest_framework import serializers


class RelatedAwardValidator:

    def __call__(self, data):
        # Исключить одновременный выбор связанной привычки и указания вознаграждения.
        related_habit = data.get('related_pleasant_habit')
        reward = data.get('reward')
        if related_habit and reward:
            raise serializers.ValidationError('Нельзя указывать одновременно связанную привычку и вознаграждение.')


class CompletionTimeValidator:

    def __call__(self, data):
        #  Время выполнения привычки должно быть не больше 2 минут
        completion_time = bool(dict(data).get("completion_time"))
        if completion_time > 2:
            raise serializers.ValidationError('Время выполнения привычки должно быть не больше 2 минут')


class PleasantHabitValidator:

    def __call__(self, data):
        #  Связанная привычка должна быть приятной
        related_habit = data.get('related_pleasant_habit')
        is_pleasant = data.get('is_pleasant')

        if related_habit and not is_pleasant:
            raise serializers.ValidationError('Связанная привычка должна быть приятной')


class HabitPleasantAwardValidator:

    def __call__(self, data):
        #  У приятной привычки не может быть вознаграждения или связанной привычки
        related_habit = data.get('related_pleasant_habit')
        reward = data.get('reward')
        is_pleasant = data.get('is_pleasant')
        if is_pleasant and reward or is_pleasant and related_habit:
            raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class FrequencyValidator:

    def __call__(self, data):
        #  Нельзя выполнять привычку реже, чем 1 раз в 7 дней
        frequency = data.get('frequency')
        if frequency < 7:
            raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')





















