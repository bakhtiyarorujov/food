from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
User = get_user_model()

class Command(BaseCommand):
    help = "Used to delete fake users."
    requires_migrations_checks = True

    def handle(self, *args, **options):
        x = User.objects.filter(is_superuser = False)
        x.delete()