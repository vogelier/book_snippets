from django.core.management.base import BaseCommand, CommandError

class GenerateFixtures(BaseCommand):
    help = 'Generates some dummy data'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write('You did it!')

