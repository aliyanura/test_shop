from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from decouple import config

class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username=config('DJANGO_SUPERUSER_USERNAME', 'admin'),
                email=config('DJANGO_SUPERUSER_EMAIL', 'admin@example.com'),
                password=config('DJANGO_SUPERUSER_PASSWORD', 'password123')
            )
            self.stdout.write("Superuser created successfully!")
        else:
            self.stdout.write("Superuser already exists.")
