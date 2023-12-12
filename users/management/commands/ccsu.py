from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            username='test',
            first_name='test',
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user.set_password('9184')
        user.save()


