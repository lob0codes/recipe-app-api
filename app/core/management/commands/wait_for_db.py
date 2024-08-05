"""
Makes sure that postgresql db finished starting its services.
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for db to be ready."""

    def handle(self, *args, **options):
        pass
